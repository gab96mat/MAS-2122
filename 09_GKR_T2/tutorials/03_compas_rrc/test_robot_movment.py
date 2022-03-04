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
PRINT_LAYERS = 3
PRINT_LAYER_HIGHT = 5

# Define vectors
xaxis = Vector(-1.000, 0.000, 0.000)
yaxis =Vector(0.000, 1.000, 0.000)

# Define points
a = Point(0,0,0)
b = Point(100,0,0)
c = Point(100,50,0)
d = Point(0,50,0)

# Make compas frames
frame_a = Frame(a, xaxis, yaxis)
frame_b = Frame(b, xaxis, yaxis)
frame_c = Frame(c, xaxis, yaxis)
frame_d = Frame(d, xaxis, yaxis)

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
    abb.send(rrc.MoveToFrame(frame_a, MAX_SPEED, rrc.Zone.FINE, motion_type=rrc.Motion.LINEAR))

    # Activate printer
    if PRINT_ON:
        abb.send(rrc.SetDigital(PRINTER_ON,1))

    # Print loop
    for i in range(1,PRINT_LAYERS):

        abb.send(rrc.MoveToFrame(frame_b, PRINT_SPEED, PRINT_BLEND, motion_type=rrc.Motion.LINEAR))
        abb.send(rrc.MoveToFrame(frame_c, PRINT_SPEED, PRINT_BLEND, motion_type=rrc.Motion.LINEAR))
        abb.send(rrc.MoveToFrame(frame_d, PRINT_SPEED, PRINT_BLEND, motion_type=rrc.Motion.LINEAR))

        # Update hight
        frame_a.point[2] += PRINT_LAYER_HIGHT
        frame_b.point[2] += PRINT_LAYER_HIGHT
        frame_c.point[2] += PRINT_LAYER_HIGHT
        frame_d.point[2] += PRINT_LAYER_HIGHT

        if not i == PRINT_LAYERS:
            abb.send(rrc.MoveToFrame(frame_a, PRINT_SPEED, PRINT_BLEND, motion_type=rrc.Motion.LINEAR))

    # Do the last move of the print
    abb.send(rrc.MoveToFrame(frame_a, PRINT_SPEED, rrc.Zone.FINE, motion_type=rrc.Motion.LINEAR))

    # Deactivate printer
    done = abb.send_and_wait(rrc.SetDigital(PRINTER_ON,0))

    # Move robot back in home position
    done = abb.send_and_wait(rrc.MoveToJoints(HOME_POSITION, [], MAX_SPEED, rrc.Zone.FINE))

    # Close client
    ros.close()
    ros.terminate()

# End
print('Print finish')

