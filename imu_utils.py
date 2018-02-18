from mpu9250 import mpu9250
import math 
ROLLING_AMOUNT = 1
direction = mpu9250().mag
direction = 180-math.degrees(math.atan2( direction[1],direction[0]))

rolling=[0,0]
def get_compass():
    global direction
	Magread = mpu9250().mag
	magx = Magread[0]
	magy = Magread[1]
	if magx==0 and magy ==0 :
		return direction
	else:
	    rolling[0]=(rolling[0]*ROLLING_AMOUNT+magx)/(ROLLING_AMOUNT+1)
	    rolling[1]=(rolling[1]*ROLLING_AMOUNT+magy)/(ROLLING_AMOUNT+1)
		val = math.atan2(rolling[1],rolling[0])
    	direction = 180-math.degrees(val)
    	return direction



def get_yaw_roc():
    """
    Get yaw rate of change
    """
    gyro = mpu9250().gyro
    return gyro[3]