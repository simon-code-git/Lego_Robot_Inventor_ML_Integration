from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.hubs import InventorHub
from usys import stdin, stdout

hub = InventorHub()
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=112)

hub.display.char('#')
stdout.buffer.write(b'Connection established.')
while True:
    cmd = stdin.buffer.read(1)
    hub.display.char(str(cmd, 'utf-8'))
    stdout.buffer.write(cmd)
    if cmd == b'9': 
        hub.speaker.beep()
    