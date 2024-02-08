# -*- coding: utf-8 -*-

import serial
import serial.tools.list_ports


def uart(port, baudrate):
    ser = serial.Serial(port=port,
                        baudrate=baudrate,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS,
                        timeout=0)
    try:
        return ser
    except Exception as ex:
        print(ex)


def getport():
    ports = []
    for port in serial.tools.list_ports.comports():
        ports.append(port.name)
    if len(ports) != 0:
        return ports[0]
