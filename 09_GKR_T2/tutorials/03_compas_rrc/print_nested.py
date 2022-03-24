import os
import json
import compas_rrc as rrc
import time

from compas.geometry import Frame, Vector

# ==============================================================================
# Set parameters
# ==============================================================================

# Switches
ROBOT_ON = False
PRINT_ON = False

# Robot confgiuration
ROBOT_TOOL = 't_A080_Extruder_Tip'
ROBOT_WORK_OBJECT = 'ob_A080_Workplace'
PRINTER_ON = 'doPrintOn'

# Home position
HOME_POSITION = [0.0, -35.0, 50.0, 0.0, 75.0, 0.0]

# Velocities
MAX_SPEED = 250
MIN_SPEED = 50

# Print settings
PRINT_SPEED = 50
PRINT_BLEND = rrc.Zone.Z0

# ==============================================================================
# Load data from json file
# ==============================================================================

# Define location of print data
DATA_OUTPUT_FOLDER = os.path.join(os.path.dirname(__file__), 'data', 'output')
PRINT_FILE_NAME = 'out_printpoints_nested.json'

# Open print data
with open(os.path.join(DATA_OUTPUT_FOLDER, PRINT_FILE_NAME), 'r') as file:
    data = json.load(file)

# Print file loaded
print('Print data loaded :', os.path.join(DATA_OUTPUT_FOLDER, PRINT_FILE_NAME))

# Define print data containers
frames_flattened = []
frames_nested = []
velocities = []
zones = []
extruder_toggles = []
wait_times = []

# iterate through the layers
for i in range(len(data)):
    paths = []
    layer_key = 'layer_' + str(i)
    # iterate through the paths
    for j in range(len(data[layer_key])):
        points = []
        path_key = 'path_' + str(j)
        # iterate through the points
        for k in range(len(data[layer_key][path_key])):

            ppt_data = data[layer_key][path_key][str(k)]
            point = ppt_data["point"]

            # define X and Y axis
            xaxis = Vector(-1.000, 0.000, 0.000)
            yaxis = Vector(0.000, 1.000, 0.000)

            # Make COMPAS frame
            frame = Frame(point, xaxis, yaxis)

            # Read fabrication data and fill containers
            velocities.append(ppt_data['velocity'])
            zones.append(ppt_data['blend_radius'])
            extruder_toggles.append(ppt_data['extruder_toggle'])
            wait_times.append(ppt_data['wait_time'])

            points.append(frame)
        paths.append(points)
    frames_nested.append(paths)

# Prints first frame
print('Frame           = ', frames_flattened[0])
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
    print('Connected.')

    # Make sure extruder is off
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

    # ===========================================================================
    # Robot movement
    # ===========================================================================

    # Move robot to home position
    start = abb.send_and_wait(rrc.MoveToJoints(HOME_POSITION, [], MAX_SPEED, rrc.Zone.FINE))

    # Iterate through the frames per layer and per path
    pt_index = 0
    for i, layer in enumerate(frames_nested):
        print("layer", i)
        for j, path in enumerate(layer):
            print("path", j)
            for k, frame in enumerate(path):
                # Loop through the frames

                # For first point, turn extruder on
                if PRINT_ON and pt_index == 0:
                    abb.send(rrc.SetDigital(PRINTER_ON, 1))

                # Optional sleep time in loop
                # time.sleep(0.01)

                # Create print instruction and send
                instruction = rrc.MoveToFrame(frame, velocities[pt_index], rrc.Zone.Z30, motion_type=rrc.Motion.LINEAR)
                abb.send(instruction)

                if pt_index == 0:
                    print(instruction)

    # Deactivate printer
    done = abb.send_and_wait(rrc.SetDigital(PRINTER_ON, 0))

    # Move robot back in home position
    done = abb.send_and_wait(rrc.MoveToJoints(HOME_POSITION, [], MAX_SPEED, rrc.Zone.FINE))

    # Close client
    ros.close()
    ros.terminate()

# End
print('Print finish')

