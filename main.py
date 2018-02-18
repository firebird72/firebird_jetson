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
        steering = 90 + 30 * controller_status[0]
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
        print(steering)

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

else: #AUTOMATIC



    import time
    import libraries.gps as gps
    import libraries.imu as imu
    import libraries.bearings as bearings
    from libraries.settings import *

    centerOfTrack = [-27.8556425, 153.151405]

    waypoints = [[-27.8552175, 153.1511374],
                 [-27.8554650, 153.1516188],
                 [-27.8557407, 153.1520735],
                 [-27.8560205, 153.1521694],
                 [-27.8560920, 153.1519464],
                 [-27.8559772, 153.1513396],
                 [-27.8555771, 153.1508628],
                 [-27.8553002, 153.1509104]]

    # [[-27.8552616667, 153.151291667],
    # [-27.8553216667, 153.151405],
    # [-27.8554266667, 153.151566667],
    # [-27.8555, 153.151725],
    # [-27.8555866667, 153.15189],
    # [-27.8557016667, 153.152083333],
    # [-27.855865, 153.152198333],
    # [-27.85597, 153.152228333],
    # [-27.8560216667, 153.152198333],
    # [-27.8560783333, 153.15216],
    # [-27.8561183333, 153.15206],
    # [-27.85611, 153.151958333],
    # [-27.856065, 153.151771667],
    # [-27.85603, 153.151628333],
    # [-27.8560016667, 153.151535],
    # [-27.85596, 153.151348333],
    # [-27.85584, 153.151086667],
    # [-27.8555833333, 153.150935],
    # [-27.8554083333, 153.150948333],
    # [-27.8553283333, 153.150986667],
    # [-27.8552716667, 153.151021667],
    # [-27.855235, 153.151121667]]

    #car.acceleration(1)
    # TODO CHECK IF THIS IS 15 percent with PAUL
    Ardu.updateGear(4)
    Ardu.convertAll()
    Ardu.sendCommands()
    time.sleep(5)

    Ardu.updateThrottle(0.15)
    Ardu.convertAll()
    Ardu.sendCommands()

    def getCoords():
        gps_success = False
        while not gps_success:
            gps_success, coords = gps.getGPS()
        return coords

    def follow_point(point):
        # Try and get GPS coordinates
        coords = getCoords()
        while bearings.coord_dist_meters(coords[0], coords[1], point[0], point[1]) > DIST_THRES_METER:
            # Get current coords long and lat
            coords = getCoords()
            if bearings.coord_dist_meters(coords[0], coords[1], centerOfTrack[0], centerOfTrack[
                1]) > TRACK_RADIUS:  # check if car is out of the track, if so stop car and wait
                # TODO
                Ardu.updateKill(1)
                Ardu.convertAll()
                Ardu.sendCommands()
                # car.stop()
                # car.send()
                print("OUT OF TRACK, KILLING ALL SYSTEMS")
                input()

            ###########ADD BLOB IF STATMENT/DETECTION HERE
            # if cv.are_blobs():
            #     follow_blob()
            ##  driveToBlob()   goto blob until blob dissapears then return to main loop

            # Calculate bearing
            coordsDirection = bearings.coord_bearing_degrees(coords[0], coords[1],  # Our location
                                                             point[0], point[1])  # waypoint location
            coordsAngleError = bearings.subtract_angles(coordsDirection, imu.getCompass())  # calculate steering error

            # print("Current Compass: ",imu.getCompass()," Coord angle: ",coordsDirection," Steer Error: ",coordsAngleError," Distance to target: ",bearings.coord_dist_meters(coords[0], coords[1], point[0], point[1]))
            print("Steering error:", coordsAngleError)
            # TODO
            A_err = coordsAngleError / 90
            Ardu.updateSteering(90 + 30 * A_err)
            Ardu.convertAll()
            Ardu.sendCommands()
            # car.steer(coordsAngleError)
            # car.send()

            time.sleep(0.01)
        Ardu.updateKill(1)
        Ardu.convertAll()
        Ardu.sendCommands()

    while True:
        for point in waypoints:
            follow_point(point)
            print("FLOWING WAYPOINT:", point)
