import os
import json
import compas_rrc as rrc
import time

from compas.geometry import Frame, Point, Vector

# Switches
ROBOT_ON = True
PRINT_ON = True

# Robot confgiuration
ROBOT_TOOL = 't_A080_Extruder_Tip'
ROBOT_WORK_OBJECT = 'ob_A080_Workplace'
PRINTER_ON = 'doPrintOn'

# Positions
HOME_POSITION = [0.0, -35.0, 50.0, 0.0, 75.0, 0.0]

# Speeds
MAX_SPEED = 250
MIN_SPEED = 50

# Print settings
PRINT_SPEED = 50
PRINT_BLEND = rrc.Zone.Z0

# Start
print('Start print')

# Define location of print data
PRINT_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', '01_compas_slicer', 'data', 'output')
PRINT_FILE_NAME = 'out_printpoints.json'
PRINT_DATA = os.path.join(PRINT_FILE_PATH, PRINT_FILE_NAME)

# Open print data
with open(PRINT_DATA, 'r') as file:
    DATA = json.load(file)

# Print file loaded
print('Print data = ',PRINT_DATA)

# Define print data containers
FRAMES = []
SPEEDS = []
ZONES = []
EXTRUDER_TOGGELS = []
WAITTIMES = []

# Move print data in data containers
for item in DATA:

    # Read frame data
    point = (DATA[item]['point'])

    # xaxis = (DATA[item]['frame']['xaxis'])
    xaxis = Vector(-1.000, 0.000, 0.000)

    # yaxis = (DATA[item]['frame']['yaxis'])
    yaxis =Vector(0.000, 1.000, 0.000)


    # Make COMPAS frame
    frame = Frame(point, xaxis, yaxis)

    # Input Gonzalo
    # frame = Frame.from_data(DATA[item]['frame'])
    # frame = DATA[item]['frame']
    # print(frame)

    # Fill containers
    FRAMES.append(frame)
    SPEEDS.append(DATA[item]['velocity'])
    ZONES.append(DATA[item]['blend_radius'])
    EXTRUDER_TOGGELS.append(DATA[item]['extruder_toggle'])
    WAITTIMES.append(DATA[item]['wait_time'])

    # Print first items
    if item == str(0):
        print('Frame           = ', FRAMES[0])
        print('Speed           = ', SPEEDS[0])
        print('Zone            = ', ZONES[0])
        print('Extruder Toggle = ', EXTRUDER_TOGGELS[0])
        print('Wait time       = ', WAITTIMES[0])

# End if robot is not on
if not ROBOT_ON:
    # End
    print('Print finish')
    exit()

# ==============================================================================
# Main robotic control function
# ==============================================================================

if __name__ == '__main__':

    # Create Ros Client
    ros = rrc.RosClient()
    ros.run()

    # Create ABB Client
    abb = rrc.AbbClient(ros, '/rob1')
    print('Connected.')

    # Printer reset
    abb.send(rrc.SetDigital(PRINTER_ON,0))

    # Set Tool
    abb.send(rrc.SetTool(ROBOT_TOOL))

    # Set Work Object
    abb.send(rrc.SetWorkObject(ROBOT_WORK_OBJECT))

    # Set Acceleration
    acc = 100  # Unit [%]
    ramp = 100 # Unit [%]
    abb.send(rrc.SetAcceleration(acc, ramp))

    # Set Max Speed
    override = 100  # Unit [%]
    max_tcp = 1000  # Unit [mm/s]
    abb.send(rrc.SetMaxSpeed(override, max_tcp))

    # Move robot to start position
    abb.send(rrc.MoveToFrame(FRAMES[0], MAX_SPEED, rrc.Zone.FINE, motion_type=rrc.Motion.LINEAR))
    #abb.send(rrc.MoveToFrame(FRAMES[int(0)], MAX_SPEED, rrc.Zone.FINE, motion_type=rrc.Motion.LINEAR))

    # Activate printer
    if PRINT_ON:
        abb.send(rrc.SetDigital(PRINTER_ON,1))

    # Print loop
    instruction = []
    for i in range(1, len(DATA)-1):

        #time.sleep(0.01)

        # print(FRAMES[int(i)])

        instruction = rrc.MoveToFrame(FRAMES[i], PRINT_SPEED, rrc.Zone.Z30, motion_type=rrc.Motion.LINEAR)

        abb.send(instruction)

        if i == str(0):
            print(instruction)

    # Do the last move of the print
    abb.send(rrc.MoveToFrame(FRAMES[-1], MAX_SPEED, rrc.Zone.FINE, motion_type=rrc.Motion.LINEAR))

    # Deactivate printer
    done = abb.send_and_wait(rrc.SetDigital(PRINTER_ON,0))

    # Move robot back in home position
    done = abb.send_and_wait(rrc.MoveToJoints(HOME_POSITION, [], MAX_SPEED, rrc.Zone.FINE))

    # Close client
    ros.close()
    ros.terminate()

# End
print('Print finish')

