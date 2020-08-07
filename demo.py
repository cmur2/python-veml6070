#!/usr/bin/env python

import veml6070

ALL_INTEGRATION_TIMES = [
    veml6070.INTEGRATIONTIME_1_2T, veml6070.INTEGRATIONTIME_1T, veml6070.INTEGRATIONTIME_2T, veml6070.INTEGRATIONTIME_4T
]

if __name__ == '__main__':
    veml = veml6070.Veml6070()
    for i in ALL_INTEGRATION_TIMES:
        veml.set_integration_time(i)
        uv_raw = veml.get_uva_light_intensity_raw()
        uv = veml.get_uva_light_intensity()
        print("Integration Time setting %d: %f W/(m*m) from raw value %d" % (i, uv, uv_raw))
