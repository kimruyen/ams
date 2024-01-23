# -*- coding: utf-8 -*-

import serial
import serial.tools.list_ports


def uart(port, baudRate):
    ser = serial.Serial(port=port,
                        baudrate=baudRate,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS,
                        timeout=1)
    try:
        ser.open()
        return ser
    except Exception as ex:
        print(ex)


def getPort():
    ports = []
    for port in serial.tools.list_ports.comports():
        ports.append(port.name)

    return ports[0]
