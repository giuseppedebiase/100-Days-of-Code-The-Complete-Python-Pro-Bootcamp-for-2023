#This code is the solution for the "Maze" level in the game "Reeborg's World" (including the edge cases presented in the three "problem_world" files)

def turn_right():
    turn_left()
    turn_left()
    turn_left()

if wall_on_right()==False and wall_in_front()==False:
        move()
        turn_left()
while at_goal()==False:
    if wall_on_right()==False:
        turn_right()
        move()
    elif wall_on_right()==True and wall_in_front()==False:
        move()
    elif wall_on_right()==True and wall_in_front()==True:
        turn_left()
