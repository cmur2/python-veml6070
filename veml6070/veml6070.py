import time

import smbus  # pylint: disable=import-error

ADDR_L = 0x38  # 7bit address of the VEML6070 (write, read)
ADDR_H = 0x39  # 7bit address of the VEML6070 (read)

RSET_240K = 240000
RSET_270K = 270000
RSET_300K = 300000
RSET_600K = 600000

SHUTDOWN_DISABLE = 0x00
SHUTDOWN_ENABLE = 0x01

INTEGRATIONTIME_1_2T = 0x00
INTEGRATIONTIME_1T = 0x01
INTEGRATIONTIME_2T = 0x02
INTEGRATIONTIME_4T = 0x03

# Scale factor in seconds / Ohm to determine refresh time for any RSET
# Note: 0.1 seconds (100 ms) are applicable for RSET_240K and INTEGRATIONTIME_1T
RSET_TO_REFRESHTIME_SCALE = 0.1 / RSET_240K

# The refresh time in seconds for which NORMALIZED_UVA_SENSITIVITY
# is applicable to a step count
NORMALIZED_REFRESHTIME = 0.1

# The UVA sensitivity in W/(m*m)/step which is applicable to a step count
# normalized to the NORMALIZED_REFRESHTIME, for RSET_240K and INTEGRATIONTIME_1T
NORMALIZED_UVA_SENSITIVITY = 0.05


class Veml6070(object):  # pylint: disable=bad-option-value,useless-object-inheritance
    def __init__(self, i2c_bus=1, sensor_address=ADDR_L, rset=RSET_270K, integration_time=INTEGRATIONTIME_1T):
        self.bus = smbus.SMBus(i2c_bus)
        self.sendor_address = sensor_address
        self.rset = rset
        self.shutdown = SHUTDOWN_DISABLE  # before set_integration_time()
        self.set_integration_time(integration_time)
        self.disable()

    def set_integration_time(self, integration_time):
        self.integration_time = integration_time
        self.bus.write_byte(self.sendor_address, self.get_command_byte())
        # constant offset determined experimentally to allow sensor to readjust
        time.sleep(0.2)

    def get_integration_time(self):
        return self.integration_time

    def enable(self):
        self.shutdown = SHUTDOWN_DISABLE
        self.bus.write_byte(self.sendor_address, self.get_command_byte())

    def disable(self):
        self.shutdown = SHUTDOWN_ENABLE
        self.bus.write_byte(self.sendor_address, self.get_command_byte())

    def get_uva_light_intensity_raw(self):
        self.enable()
        # wait two times the refresh time to allow completion of a previous cycle with old settings (worst case)
        time.sleep(self.get_refresh_time() * 2)
        msb = self.bus.read_byte(self.sendor_address + (ADDR_H - ADDR_L))
        lsb = self.bus.read_byte(self.sendor_address)
        self.disable()
        return (msb << 8) | lsb

    def get_uva_light_intensity(self):
        """
        returns the UVA light intensity in Watt per square meter (W/(m*m))
        """
        raw_data = self.get_uva_light_intensity_raw()

        # normalize raw data (step count sampled in get_refresh_time()) into the
        # linearly scaled normalized data (step count sampled in 0.1s) for which
        # we know the UVA sensitivity
        normalized_data = raw_data * NORMALIZED_REFRESHTIME / self.get_refresh_time()

        # now we can calculate the absolute UVA power detected combining
        # normalized  data with known UVA sensitivity for this data
        return normalized_data * NORMALIZED_UVA_SENSITIVITY  # in W/(m*m)

    def get_command_byte(self):
        """
        assembles the command byte for the current state
        """
        cmd = (self.shutdown & 0x01) << 0  # SD
        cmd = cmd | (self.integration_time & 0x03) << 2  # IT
        cmd = ((cmd | 0x02) & 0x3F)  # reserved bits
        return cmd

    def get_refresh_time(self):
        """
        returns time needed to perform a complete measurement using current settings (in s)
        """
        case_refresh_it = {
            INTEGRATIONTIME_1_2T: 0.5,
            INTEGRATIONTIME_1T: 1,
            INTEGRATIONTIME_2T: 2,
            INTEGRATIONTIME_4T: 4
        }
        return self.rset * RSET_TO_REFRESHTIME_SCALE * case_refresh_it[self.integration_time]

    @staticmethod
    def get_estimated_risk_level(intensity):
        """
        returns estimated risk level from comparing UVA light intensity value
        in W/(m*m) as parameter, thresholds calculated from application notes
        """
        if intensity < 24.888:
            return "low"
        if intensity < 49.800:
            return "moderate"
        if intensity < 66.400:
            return "high"
        if intensity < 91.288:
            return "very high"
        return "extreme"
