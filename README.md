# python-veml6070

[![Build Status](https://travis-ci.org/cmur2/python-veml6070.svg?branch=master)](https://travis-ci.org/cmur2/python-veml6070)

A Python library for accessing the [VEML6070 digital UV light sensor](http://www.vishay.com/docs/84277/veml6070.pdf) from Vishay via `python-smbus` using the I2C interface.

Default settings are suitable for Raspberry Pi 2 and 3 and was successfully tested using a [breakout](https://github.com/watterott/VEML6070-Breakout).

I created this Python library in style of e.g. [python-tsl2591](https://github.com/maxlklaxl/python-tsl2591) (of the TSL2591 light sensor) since I found either [python code](https://github.com/ControlEverythingCommunity/VEML6070) broken for my hardware or [code targeted at Arduino](https://github.com/kriswiner/VEML6070).

## Usage

Consult the [datasheet](https://www.vishay.com/docs/84277/veml6070.pdf), the [application notes](https://www.vishay.com/docs/84310/designingveml6070.pdf) and see [demo.py](demo.py) for clues how to use this library.

Not all functions of the chip are supported, especially not the interrupt handling since I had no use for this. Please send pull requests for improvements and bug fixes!

## Serious Flaws before September 2019

In September 2019 it was discovered (and fixed) that:

- previously the sensor was never shutdown between measurements which wastes power but still takes measurements successfully
- the UVA light intensity was calculated wrongly (too high) for `rset != RSET_240K` due to wrong compensation: higher `rset` leads to higher sampling time leads to higher absolute ADC step counts which *should* lead to every ADC step indicating a smaller amount of `W/(m*m)` of UVA power and a higher precision of the final UVA power but it wrongly behaved the opposite way. The `integration_time` worked correctly all the time.

## Develop

Run `make help` to find out about the available development commands.

## License

Python files in this repository are released under the [MIT license](LICENSE).
