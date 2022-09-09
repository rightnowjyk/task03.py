from cs1robots import *

load_world("worlds/newspaper.wld")
hubo = Robot(beepers=1)
hubo.set_trace("blue")
hubo.set_pause(0.1)

def turn_right(robot):
    for i in range(3):
        robot.turn_left()

def up_stair(robot):
    for i in range(4):
        robot.turn_left()
        robot.move()
        turn_right(hubo)
        robot.move()
        robot.move()        
        
def down_stair(robot):
    for i in range(4):
        hubo.move()
        hubo.move()
        hubo.turn_left()
        hubo.move()
        turn_right(hubo)
        
hubo.move()
up_stair(hubo)

hubo.turn_left()
hubo.turn_left()

down_stair(hubo)
hubo.move()
