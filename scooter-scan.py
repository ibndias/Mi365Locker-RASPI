from bluepy import btle
from bluepy.btle import Scanner, DefaultDelegate
from bluepy.btle import BTLEDisconnectError
from bluepy.btle import BTLEGattError
import codecs
import signal
import sys
import os

TIMEOUT_LENGTH = 1
LOCK = "55aa032003700168ff"
UNLOCK = "55aa032003710167ff"

print(sys.argv[1:])

def timeout_handler(signum, frame):
    raise TimeoutError


signal.signal(signal.SIGALRM, timeout_handler)


class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)


def write_command(device, command):
    signal.alarm(TIMEOUT_LENGTH)
    peri = btle.Peripheral(device)
    characteristics = peri.getCharacteristics(uuid="6e400002-b5a3-f393-e0a9-e50e24dcca9e")[0]
    characteristics.write(codecs.decode(command, 'hex'))
    peri.disconnect()
    print("Success!")
    f = open("scootersAddr.txt", "a")
    f.write(device.addr + '\n')
    f.close()


scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(2)

print("Found ", len(devices), " device/s in bluetooth area")

fileExists = os.path.exists('./scootersAddr.txt')

if fileExists:
    with open('scootersAddr.txt') as file:
        knownAddr = file.readlines()

    for device in devices:
        for addr in knownAddr:
            if device.addr == addr:
                devices = device + devices

for device in devices:
    try:
        print("Attempting to lock device ", device.addr, device.getScanData())
        write_command(device, UNLOCK)
    except (BTLEDisconnectError, BTLEGattError, TimeoutError):
        print("Couldn't connect")
