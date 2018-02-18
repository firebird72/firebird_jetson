import numpy as np
import serial
import time


class ArduinoMap:
    def __init__(self, COM, baud):

        try:
            self.ser = serial.Serial(timeout=0)
            self.ser.port = COM
            self.ser.baudrate = baud
            self.ser.open()
        except:
            print("No Connection")
            quit()
        self.gearlookup = [267, # P
                           312, # R
                           367, # N
                           417, # D
                           457, # 3
                           508, # 2
                           540] # L

    def readSerial(self):
        return self.ser.readline()

    def updateSteering(self, newSteer):
        """updates steering angle ( between -900 and 900 )"""
        self.steering = np.clip(newSteer, 60, 120)

    def updateBrake(self, newBrake):
        """ updates braking percentage"""
        self.brake = np.clip(newBrake, 0.0, 1.0)

    def updateThrottle(self, newThrottle):
        """updates throttle as a percentage"""
        self.throttle = np.clip(newThrottle, 0.0, 1.0)

    def updateGear(self, newGear):
        """udates gear as a 0 indexed integer """
        self.gear = np.clip(newGear, 0, 5)

    def updateAuto(self, newAuto):
        """Changes modes from autonomous to RC car """
        self.auto = np.clip(newAuto, 0, 1)

    def updateIgnition(self, newIgnition):
        """Using ignition relays to start car and starter motor """
        self.ignition = np.clip(newIgnition, 0, 1)

    def updateKill(self, newKill):
        """Changes mode from alive to dead """
        self.kill = np.clip(newKill, 0, 1)

    def update(self, newSteer, newBrake, newThrottle, newGear, newAuto, newIgnition, newKill):
        """Updates all with defaults """
        self.steering = np.clip(newSteer, -900, 900)
        self.brake = np.clip(newBrake, 0, 100)
        self.throttle = np.clip(newThrottle, 0, 100)
        self.gear = np.clip(newGear, 0, 5)
        self.auto = np.clip(newAuto, 0, 1)
        self.ignition = np.clip(newIgnition, 0, 1)
        self.kill = np.clip(newKill, 0, 1)

    def convertAll(self):
        self.steeringArdu = np.clip(int(self.steering), 60, 120)
        self.brakeArdu = np.clip(int(385 + self.brake * (550-385)), 385, 550)
        self.throttleArdu = np.clip(int(120 - 40 * self.throttle), 80, 120)
        self.gearArdu = self.gearlookup[self.gear]
        self.checksum = self.steeringArdu + self.brakeArdu + self.throttleArdu + self.gearArdu

    def sendCommands(self):
        string = ""
        string += str(self.steeringArdu).zfill(4)
        string += str(self.brakeArdu).zfill(4)
        string += str(self.throttleArdu).zfill(4)
        string += str(self.gearArdu).zfill(4)
        string += str(self.auto)
        string += str(self.ignition)
        string += str(self.kill)
        string += str(self.checksum).zfill(4)
        string += "\n"
        print(string)
        try:
            self.ser.write(string.encode())
        except:
            pass

    def arduinoSerial(self, newSteer, newBrake, newThrottle, newGear, newAuto, newIgnition, newKill):
        self.update(newSteer, newBrake, newThrottle, newGear, newAuto, newIgnition, newKill)
        self.convertAll()
        self.sendCommands()

    def Default(self):
        self.update(0, 100, 0, 0, 1, 0, 0)
        self.convertAll()
        self.sendCommands()







