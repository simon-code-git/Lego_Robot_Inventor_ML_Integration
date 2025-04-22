from pybricks.parameters import Port
from pybricks.hubs import InventorHub
from usys import stdin, stdout
from pybricks.pupdevices import UltrasonicSensor
from pybricks.tools import wait

hub = InventorHub()
sensor = UltrasonicSensor(Port.D)

hub.display.char('U')
while True: 
    reading = sensor.distance()
    stdout.buffer.write(bytes(str(reading), 'utf-8'))
    wait(100)
    