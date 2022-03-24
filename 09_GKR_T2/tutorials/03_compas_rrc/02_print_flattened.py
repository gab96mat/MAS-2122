import os
import json
import compas_rrc as rrc
import time

from compas.geometry import Frame, Vector
from sympy import I

# ==============================================================================
# Set parameters
# ==============================================================================

# Switches
ROBOT_ON = True
PRINT_ON = True

# Robot confgiuration
ROBOT_TOOL = 't_A080_Extruder_Tip'
ROBOT_WORK_OBJECT = 'ob_A080_Workplace'
PRINTER_ON = 'doPrintOn'

# Home position
HOME_POSITION = [0.0, -35.0, 50.0, 0.0, 75.0, 0.0]

# Velocities
MAX_SPEED = 250
MIN_SPEED = 50

# ==============================================================================
# Load data from json file
# ==============================================================================

# Define location of print data
DATA_OUTPUT_FOLDER = os.path.join(os.path.dirname(__file__), 'data', 'output')
PRINT_FILE_NAME = 'out_printpoints_flat.json'

# Open print data
with open(os.path.join(DATA_OUTPUT_FOLDER, PRINT_FILE_NAME), 'r') as file:
    data = json.load(file)

# Print file loaded
print('Print data loaded :', os.path.join(DATA_OUTPUT_FOLDER, PRINT_FILE_NAME))

# Define print data containers
frames = []
velocities = []
zones = []
extruder_toggles = []
wait_times = []

for item in data:
    # Read frame data
    point = (data[item]['point'])
    xaxis = Vector(-1.000, 0.000, 0.000)
    yaxis =Vector(0.000, 1.000, 0.000)

    # Make COMPAS frame
    frame = Frame(point, xaxis, yaxis)

    # Fill containers
    frames.append(frame)
    velocities.append(data[item]['velocity'])
    zones.append(data[item]['blend_radius'])
    extruder_toggles.append(data[item]['extruder_toggle'])
    wait_times.append(data[item]['wait_time'])

# Prints first frame
print('Frame           = ', frames[0])
print('Speed           = ', velocities[0])
print('Zone            = ', zones[0])
print('Extruder Toggle = ', extruder_toggles[0])
print('Wait time       = ', wait_times[0])

# End if robot is not on
if not ROBOT_ON:
    # End
    print('Finish code without moving robot')
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
    print('Connected')

    # Make sure extruder is off
    abb.send(rrc.SetDigital(PRINTER_ON, 0))

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

    # ===========================================================================
    # Robot movement
    # ===========================================================================
    print("Starting print")

    # Move robot to home position
    start = abb.send_and_wait(rrc.MoveToJoints(HOME_POSITION, [], MAX_SPEED, rrc.Zone.FINE))

    # Move robot to first frame
    start = abb.send_and_wait(rrc.MoveToFrame(frames[0], MAX_SPEED, rrc.Zone.FINE, rrc.Motion.LINEAR))

    if PRINT_ON:
        abb.send(rrc.SetDigital(PRINTER_ON, 1))

    for i in range(1, len(frames)-1):
        # Optional sleep time in loop
        # time.sleep(0.01)

        # Create print instruction and send
        instruction = rrc.MoveToFrame(frames[i], velocities[i], rrc.Zone.Z5, motion_type=rrc.Motion.LINEAR)
        abb.send(instruction)

    # Do the last move of the print
    abb.send(rrc.MoveToFrame(frames[-1], MAX_SPEED, rrc.Zone.FINE, motion_type=rrc.Motion.LINEAR))

    # Deactivate printer
    done = abb.send_and_wait(rrc.SetDigital(PRINTER_ON, 0))

    # Move robot back in home position
    done = abb.send_and_wait(rrc.MoveToJoints(HOME_POSITION, [], MAX_SPEED, rrc.Zone.FINE))

    # Close client
    ros.close()
    ros.terminate()

# End
print('Print finish')

