import math 

# def get_compass():

# 	imu = FaBo9Axis_MPU9250.MPU9250()
# 	accel = mpu9250.readAccel()
# 	gyro = mpu9250.readGyro()
# 	mag = mpu9250.readMagnet()
# 	if mag['x'] == 0.0 and mag['y'] == 0.0:
# 		return direction # We are aligned properly 
# 	else:
# 		val = math.atan2(rolling[1],rolling[0])
# 		return 180 - math.degrees(val)

# def get_yaw_ROC():
# 	gyro = mpu9250.readGyro()
# 	return gyro['y']
from mpu9250 import mpu9250
from time import sleep

imu = mpu9250()

def get_compass():
	a = imu.mag
	print(a)
	# while True:
	# 	a = imu.accel
	# 	print 'Accel: {:.3f} {:.3f} {:.3f} mg'.format(*a)
	# 	# g = imu.gyro
	# 	# print 'Gyro: {:.3f} {:.3f} {:.3f} dps'.format(*g)
	# 	# m = imu.mag
	# 	# print 'Magnet: {:.3f} {:.3f} {:.3f} mT'.format(*m)
	# 	# m = imu.temp
	