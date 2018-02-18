# Serial port settings
CAR_SERIAL_PORT = '/dev/ttyUSB1'
GPS_SERIAL_PORT = '/dev/ttyUSB0'

# How far do we have to be from a point
# before we consider it to be 'close enough'
DIST_THRES_METER = 10


#radius of trak used for GPS kill switch
TRACK_RADIUS=120

# Compass rolling average
ROLLING_AMOUNT = 1

# Image properties
IMAGE_WIDTH = 720
IMAGE_HEIGHT = 720

# Color thresholding
RADIUS = 10
RED_THRES_LOW = (160, 120, 20)
RED_THRES_HIGH = (185, 220, 200)
