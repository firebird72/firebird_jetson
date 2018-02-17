from threading import Thread
from controller import JoystickController

import time
from python_to_arduino import ArduinoMap
# Main logic for jetson on firebird

# ######### TWEAK PARAMS

Ardu = ArduinoMap('/dev/ttyACM0', 9600)
# TODO How to read 3 pos switch
manual = True

ctr = JoystickController(auto_record_on_throttle=False)

t = Thread(target=ctr.update, args=())
t.daemon = True
t.start()

inputs = [],

# outputs=['user/angle', 'user/throttle', 'user/mode', 'recording', "x_button"],
# while True:
#     outputs = ctr.run_threaded(inputs)
#     print("button status " + str(outputs))
#     time.sleep(0.1)
button_map = {
    'a': 3,
    'b': 4,
    'x': 5,
    'y': 6,
    'select': 7,
    'start': 8,
    'tl': 9,
    'tr': 10,
    "lt": 11,
    "rt": 12
}


def start_button_pressed():
    outputs = ctr.run_threaded(inputs)
    return outputs[8]


def flush_serial():
    while True:
        return_str = Ardu.readSerial()
        if len(return_str) == 0:
            break


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
# ######### SELF TEST
# reset all positions
# centre steering wheel
# reset pedals
# does steering work?
# do the acutators work?
#

print("Press start to set defaults")
while True:
    flush_serial()
    if start_button_pressed():
        break

Ardu.Default()

# Ardu.updateIgnition(1)

print("Defaults set, Press start button to continue")
time.sleep(1)
# ########## Startup sequence
# # Ignition On
# # engage, wait, and disengage starter
# # Wait for GPS Lock
# Ardu.updateAuto(0)
# Ardu.convertAll()
# Ardu.sendCommands()

while True:
    flush_serial()
    if start_button_pressed():
        break
# AND OFF WE GO
#
print("now entering live mode")
if manual:

    while True:
        controller_status = ctr.run_threaded(inputs)
        # print(controller_status)
        steering = 900 * controller_status[0]
        # throtbrake = controller_status[1]
        # if throtbrake > 0.0:
        #     throttle = 100*throtbrake
        #     brake = 0
        # else:
        #     throttle = 0
        #     brake = 100*throtbrake
        throttle = ((controller_status[button_map['rt']] + 1) / 2)
        brake = ((controller_status[button_map['lt']] + 1) / 2)

        print(brake)
        print(throttle)

        if controller_status[button_map['a']]:
            Ardu.updateGear(4)
        elif controller_status[button_map['b']]:
            Ardu.updateGear(1)
        elif controller_status[button_map['y']]:
            Ardu.updateGear(2)
        if controller_status[button_map['select']]:
            Ardu.updateKill(1)

        Ardu.updateBrake(brake)
        Ardu.updateThrottle(throttle)
        Ardu.updateSteering(steering)
        Ardu.convertAll()
        Ardu.sendCommands()
        time.sleep(0.1)
        flush_serial()


# else: #AUTOMATIC
#     while True:
#         # MAIN LOOP:
#         location = gps_utils.get_curr_pos()
#         if gps_utils.waypoint_complete():
#             gps_utils.set_next_waypoint()
#         #Any other status?
#         if gps_utils.waypoint_reached():
