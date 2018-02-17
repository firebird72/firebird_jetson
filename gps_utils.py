
import serial
import pynmea2
import sys
import math
class gps_utils:
    def __init__(self):
                
        # GPS CONFIG MACROS
        PMTK_SET_NMEA_BAUDRATE = '$PMTK251,9600*17'
        PMTK_SET_NMEA_UPDATE_5HZ = "$PMTK220,200*2C"
        PMTK_SET_NMEA_OUTPUT_RMCONLY = '$PMTK314,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0*29'
        PMTK_SET_NMEA_OUTPUT_RMCGGA = "$PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0*28"
        PMTK_SET_NMEA_OUTPUT_GGAONLY = "$PMTK314,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0*29"
                # GPS CONFIG ROUTINE
        serial_gps = serial.Serial()
        serial_gps.port = '/dev/ttyUSB0'
        serial_gps.baudrate = 9600
        serial_gps.open()
        serial_gps.write(PMTK_SET_NMEA_BAUDRATE + '\r\n')
        serial_gps.write(PMTK_SET_NMEA_OUTPUT_GGAONLY + '\r\n')
        serial_gps.write(PMTK_SET_NMEA_UPDATE_5HZ + '\r\n')
        self.waypoint_set = [[-27.8552616667, 153.151291667],
             [-27.8553216667, 153.151405],
             [-27.8554266667, 153.151566667],
             [-27.8555, 153.151725],
             [-27.8555866667, 153.15189],
             [-27.8557016667, 153.152083333],
             [-27.855865, 153.152198333],
             [-27.85597, 153.152228333],
             [-27.8560216667, 153.152198333],
             [-27.8560783333, 153.15216],
             [-27.8561183333, 153.15206],
             [-27.85611, 153.151958333],
             [-27.856065, 153.151771667],
             [-27.85603, 153.151628333],
             [-27.8560016667, 153.151535],
             [-27.85596, 153.151348333],
             [-27.85584, 153.151086667],
             [-27.8555833333, 153.150935],
             [-27.8554083333, 153.150948333],
             [-27.8553283333, 153.150986667],
             [-27.8552716667, 153.151021667],
             [-27.855235, 153.151121667]]
        self.waypoint_idx = -1
        self.destination = None
        self.waypoint = self.waypoint_set7[[]]

    
    def wait_for_gps_lock(self):
        count = 1
        while self.get_gps[0] == False:
            count += 1
        return True


    def update_waypoint(self):
        self.waypoint_idx += 1 
        self.wa
        deltaLat = self.latitude - 

        # This is the waypoint logic where the `destination' is 5 meters past the mark.
        # get current
        # get next and set next
        # calculate
        return

    def waypoint_reached(self):
        if abs(self.latitude - self.waypoint_set[self.waypoint_idx][0]) < 5 and (self.longitude - self.waypoint_set[self.waypoint_idx][1] )<5 :
            self.update_waypoint()
        return
        # check if within X meters of next waypoint. NOT NEXT DESTINATION TARGET.

    def get_gps(self,NUM_SATS_NEEDED=4):
    	msg = ""
    	try:
    		for line in serial_gps.read():
    			line = serial_gps.readline()
    			try: # try statement so that GGAONLY doesn't catch the initial line and crash
    				msg = pynmea2.parse(line, check=True)
    			except:
    				#print('bad line for GGAONLY')
    				return False, msg
    			try:
    				#print("GPS Data: ", msg)
    				#print(msg.latitude)
    				#print(msg.longitude)
    				if int(msg.num_sats) >= NUM_SATS_NEEDED:
    					return True, msg
    				else :
    					return False, msg
    			except:
    				#print("bad GPS signal or GGAONLY invoked")
    				return False, msg
    	except:
    		return False, msg

    def get_lat_long(self):
        flag,msg =self.get_gps()
        if flag :
            self.latitude = msg.latitude
            self.longitude = msg.longitude
            # return (msg.latitude,msg.longitude)
