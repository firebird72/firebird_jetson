import array
import time
import struct
from threading import Thread
from controller import JoystickController

ctr = JoystickController()

t = Thread( target=ctr.update, args=() )
t.daemon = True
t.start()

inputs=[],
outputs=['user/angle', 'user/throttle', 'user/mode', 'recording'],

while True:
	outputs = ctr.run_threaded(inputs)
	time.sleep(1)

t.shutdown()

