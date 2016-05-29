
# python-veml6070

A Python library for accessing the [VEML6070 digital UV light sensor](http://www.vishay.com/docs/84277/veml6070.pdf) from Vishay via `python-smbus` using the I2C interface.

Default settings are suitable for Raspberry Pi 2 and 3 and was successfully tested using a [breakout](https://github.com/watterott/VEML6070-Breakout).

I created this Python library in style of e.g. [python-tsl2591](https://github.com/maxlklaxl/python-tsl2591) (of the TSL2591 light sensor) since I found either [python code](https://github.com/ControlEverythingCommunity/VEML6070) broken for my hardware or [code targeted at Arduino](https://github.com/kriswiner/VEML6070).

## Usage

Consult the data sheet and see [demo.py](demo.py) for clues how to use this library.

Not all functions of the chip are supported, especially not the interrupt handling since I had no use for this. Please send pull requests for improvements and bug fixes!

## License

Python files in this repository are released under the [MIT license](LICENSE).
