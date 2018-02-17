import time
from python_to_arduino import ArduinoMap
#Main logic for jetson on firebird

########## TWEAK PARAMS

#Ardu = ArduinoMap.ArduinoMap(99999999,99999999)
#TODO How to read 3 pos switch
manual = True

from threading import Thread
from controller import JoystickController

ctr = JoystickController( auto_record_on_throttle=False)

t = Thread( target=ctr.update, args=())
t.daemon = True
t.start()

inputs=[],
# outputs=['user/angle', 'user/throttle', 'user/mode', 'recording', "x_button"],
# while True:
#     outputs = ctr.run_threaded(inputs)
#     print("button status " + str(outputs))
#     time.sleep(0.1)

def button_pressed():
    outputs = ctr.run_threaded(inputs)
    return outputs[4]

ideas = None
#
# ########## Power On
# while True:
#     # Check if all sensors can be read
#     # IF MANUAL wait for user input
#     check
#     if (manual and button_pressed):
#         break
#
########## SELF TEST
# reset all positions
# centre steering wheel
# reset pedals
# does steering work?
# do the acutators work?
#

while True:
    if button_pressed():
        break

ArduinoMap.Default()
time.sleep(10)

# ########## Startup sequence
# # Ignition On
# # engage, wait, and disengage starter
# # Wait for GPS Lock
ArduinoMap.updateAuto(1)
ArduinoMap.convertAll()
ArduinoMap.sendCommands()

while True:
    if button_pressed():
        break
# AND OFF WE GO
#
if manual:
    ArduinoMap.updateGear(5) # Low Gear? P R N D 2 L
    ArduinoMap.updateAuto(1) #TODO CONFIRM
    ArduinoMap.convertAll()
    ArduinoMap.sendCommands()
#     # relinquish logic to user
    time.sleep(3)

    while True:
        controller_status = ctr.run_threaded(inputs)
        steering = controller_status[0]
        throtbrake = controller_status[1]
        if throtbrake > 0.0:
            throttle = 100*throtbrake
            brake = 0
        else:
            throttle = 0
            brake = 100*throtbrake
        ArduinoMap.updateBrake(brake)
        ArduinoMap.updateThrottle(throttle)
        ArduinoMap.convertAll()
        ArduinoMap.sendCommands()
# else: #AUTOMATIC
#     while True:
#         # MAIN LOOP:
#         location = gps_utils.get_curr_pos()
#         if gps_utils.waypoint_complete():
#             gps_utils.set_next_waypoint()
#         #Any other status?
#         if gps_utils.waypoint_reached():
