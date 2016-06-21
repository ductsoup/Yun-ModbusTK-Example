# Yun-ModbusTK-Example
A Modbus TCP slave example for Arduino Yun that uses the modbus-tk library.

##Overview

This example uses the modbus-tk library to implement Modbus on the Yun's AR9331 processor to conserve resources on the ATmega32u4 processor. Data is passed between the two processors using the Bridge library.

http://arduino.cc/en/Guide/ArduinoYun#toc16

Data is passed to external Modbus masters using the modbus-tk library.

https://code.google.com/p/modbus-tk

##Installation

1. Complete the initial Yun setup (http://arduino.cc/en/Guide/ArduinoYun)
2. Copy the modbus-tk library to a microSD card or jump drive and follow the installation instructions, also copy the modbus_tcp_slave.py script
3. Upload and run the example sketch

##Usage
Once installed, the modbus_tcp_slave.py script is configured and launched from the Arduino sketch. This example uses only Holding Register (float). Other encodings can easily be implemented with minor modifications to the Python script.

##Performance

On the AVR side the sketch uses about 57% of progam storage space. On the OpenWrt side the bridge and slave scripts consume about 25% of memory and 20% CPU.

##Troubleshooting

If you're having trouble with Modbus address errors there's a very good tutorial from Control Solutions Minnesota here: 

(http://www.csimn.com/CSI_pages/Modbus101.html)
