import numpy as np
import serial
import time

class JetsonMap:
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

    # zfill returns a copy of the string with zero padding to ensure width (passed as param)
# def sendCommands(self):
#     string = ""
#     string += str(self.steeringArdu).zfill(4)
#     string += str(self.brakeArdu).zfill(4)
#     string += str(self.throttleArdu).zfill(4)
#     string += str(self.gearArdu).zfill(4)
#     string += str(self.auto)
#     string += str(self.ignition)
#     string += str(self.kill)
#     string += str(self.checksum).zfill(4)
#     string += "\n"
#     print(string)
#     try:
#         self.ser.write(string.encode())
#     except:
#         pass

# is the port pre-set or a param?
def getCommands(self):
    string = readSerial()
    print(string)
    self.steeringJetson = string[0:4]
    self.brakeJetson = string[4:8]
    self.throttleJetson = string[8:12]
    self.gearJetson = string[12:16]
    self.auto = string[16]
    self.ignition = string[17]
    self.kill = string[18]
    self.checksum = string[18:23]

# def convertAll(self):
#         self.steeringArdu = np.clip(int((self.steering / 900) * 512 + 512), 0, 1023)
#         self.brakeArdu = np.clip(int(self.brake * 512), 0, 1023)
#         self.throttleArdu = np.clip(int(self.throttle * 512), 0, 1023)
#         self.gearArdu = self.gearlookup[self.gear]
#         self.checksum = self.steeringArdu + self.brakeArdu + self.throttleArdu + self.gearArdu

def convertAll(self):
    self.steeringJetson = int(self.steering * (900/512) - 512
    self.brakeJetson = int(self.brake/512)
    self.throttleJetson = int(self.throttle/512
    self.gearJetson = self.gearlookup[self.gear]
    self.checksum = self.steeringJetson + self.brakeJetson + self.throttleJetson + self.gearJetson

def updateAll(self):
    

