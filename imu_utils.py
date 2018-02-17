import FaBo9Axis_MPU9250
import math 

def get_compass():

	imu = FaBo9Axis_MPU9250.MPU9250()
	accel = mpu9250.readAccel()
	gyro = mpu9250.readGyro()
	mag = mpu9250.readMagnet()

	 if mag['x'] == 0.0 and mag['y'] == 0.0:
        return direction # We are aligned properly 
     else:
     	val = math.atan2(rolling[1],rolling[0])
     	return 180 - math.degrees(val)

def get_yaw_ROC():
	gyro = mpu9250.readGyro()
	return gyro['Y']





