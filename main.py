

#Main logic for jetson on firebird

########## TWEAK PARAMS




########## Power On
while True:
    # Check if all sensors can be read
    # IF MANUAL wait for user input
    if conditions:
        break

########## SELF TEST
# reset all positions
# centre steering wheel
# reset pedals
while True:
    # does steering work?
    # do the acutators work?

    # do I need human input to continue?
    if conditions:
        breaks

########## Startup sequence
# Ignition On
# engage, wait, and disengage starter
# Wait for GPS Lock
while True:
    if not ignition_initiated:
        start_ignition()
    ignition_complete = check_ignition()
    if ignition_complete:
        wait_for_GPS_lock()



    if conditions_are_met:
        break

# AND OFF WE GO

if manual:
    # relinquish logic to user

else: #AUTOMATIC
    while True:
        # MAIN LOOP:
        location = gps_utils.get_curr_pos()
        if gps_utils.waypoint_complete():
            gps_utils.set_next_waypoint()
        #Any other status?
        gps_utils.get