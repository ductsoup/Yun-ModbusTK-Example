#!/usr/bin/env python
# -*- coding: utf_8 -*-
"""
 Usage:
 server.py roStart roLength [rwStart rwLength]
"""

import sys
import time

# add logging capability
import logging
import threading

# add modbus
import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus as modbus
import modbus_tk.modbus_tcp as modbus_tcp
import struct

# add bridge
sys.path.insert(0, '/usr/lib/python2.7/bridge/')
from bridgeclient import BridgeClient as bridgeclient
avr = bridgeclient()

logger = modbus_tk.utils.create_logger(name="console", record_format="%(message)s")

if __name__ == "__main__":

  try:
    #Create the server
    server = modbus_tcp.TcpServer(address='0.0.0.0')
    logger.info("running...")

    server.start()
    slave_1 = server.add_slave(1)

    # todo: add checking for overlaping ranges
    argc = len(sys.argv)
    if argc == 3 or argc == 5:
      logger.info("Initializing %s RO float registers beginning at %s" % (str(sys.argv[2]), str(sys.argv[1])))
      slave_1.add_block('ro', cst.HOLDING_REGISTERS, int(sys.argv[1]), int(sys.argv[2]))
      ro = range(int(sys.argv[1]), int(sys.argv[1]) + int(sys.argv[2]))
    if argc == 5:
      logger.info("Initializing %s RW float registers beginning at %s" % (str(sys.argv[4]), str(sys.argv[3])))
      slave_1.add_block('rw', cst.HOLDING_REGISTERS, int(sys.argv[3]), int(sys.argv[4]))
      rw = range(int(sys.argv[3]), int(sys.argv[3]) + int(sys.argv[4]))

    while True:
      # get values from the bridge
      for i in ro[0::2]:
        i1,i2 = struct.unpack('>HH',struct.pack('f',float(avr.get(str(i)))))
        slave_1.set_values('ro', i, i2)
        slave_1.set_values('ro', i+1, i1)

      # put values to the bridge
      for i in rw[0::2]:
        i2, i1 = slave_1.get_values('rw', i, 2)
        val = struct.unpack('f',struct.pack('>HH',i1,i2))[0]
        avr.put(str(i),'%s' % val)

      time.sleep(0.5)

  finally:
    server.stop()
