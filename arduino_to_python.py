import numpy as np
import serial
import time

class JetsonMap:
    def __init__(self, COM, baud):

        self.gearlookup = [267, # P
                           312, # R
                           367, # N
                           417, # D
                           457, # 3
                           508, # 2
                           540] # L

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

    print("SteeringJetson: " + steeringJetson)

def convertAll(self):
    self.steeringJetson = int(self.steering * (900/512) - 512)
    self.brakeJetson = int(self.brake/512)
    self.throttleJetson = int(self.throttle/512)
    self.gearJetson = self.gearlookup[self.gear]
    self.checksum = self.steeringJetson + self.brakeJetson + self.throttleJetson + self.gearJetson

def checkHazards(self):
    getCommands(self) 
    convertAll(self)

def detectHazards(self):
    print()
