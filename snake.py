from random import randint
from psychopy import visual, event
from utilities import map_grid_to_win

def create_snake(win, square_size, position=None):
    """
    Creates a snake with the length of one segment
    at a random place by default. \n
    The position may optionally be specified with the help of
    position argument. \n
    The function returns a snake object embedded in a list
    since new segments of snake might be added later with the
    help of add_segment() function.
    """
    if position == None:
        pos = map_grid_to_win(
            (randint(0, 31), randint(0, 31)),
            square_size
        )
    else:
        pos = position

    snake = visual.Rect(win, size = square_size,
                        pos = pos, fillColor="green")

    return [snake]

def add_segment(win, snake, position, square_size):

    segment = visual.Rect(win, size = square_size,
                        pos = position, fillColor="green")

    return snake.append(segment)

def draw_snake(win, snake):
    """
    Takes the list of snake's segments as input
    and draws them.
    """
    for segment in snake:
        segment.draw()
    win.flip()