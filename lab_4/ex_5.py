#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_2():

    while wall_is_on_the_right() == True:
        move_up()
    while wall_is_on_the_left() == True:
        move_up()
    while wall_is_above() == True:
        move_right()
    while wall_is_beneath() == True:
        move_right()



if __name__ == '__main__':
    run_tasks()
