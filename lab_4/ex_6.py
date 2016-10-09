#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_3():
    while wall_is_on_the_right() == False:
        move_right()
    while wall_is_above() == False:
        move_up()
    for i in range(19):
     for j in range(9):
        if i % 2 == 0:
            move_down()
            # if wall_is_beneath() == True:
            #     move_left()
        else:
            move_up()
            # if wall_is_up() == True:
            #     move_left()

        j = j + 1

     move_left()
     i = i + 1

     # while wall_is_on_the_left() == True:
     #    move_up()
     # while wall_is_above() == True:
     #    move_right()
     # while wall_is_beneath() == True:
     #    move_right()

if __name__ == '__main__':
    run_tasks()
