class gps_utils:
    def __init__(self):
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
        self.waypoint = None

    def wait_for_gps_lock(self):
        return

    def update_waypoint(self):
        self.waypoint_idx += 1

        # This is the waypoint logic where the `destination' is 5 meters past the mark.
        # get current
        # get next and set next
        # calculate
        return

    def waypoint_reached(self):
        return
        # check if within X meters of next waypoint. NOT NEXT DESTINATION TARGET.


