from random import randint
from psychopy import visual, event
from utilities import map_grid_to_win

def create_apple(win, square_size, snake):
    """
    Creates an apple at a random place. \n
    Snake argument transmits snake's current position
    in order to avoid generating apple at the same position
    where the snake is.
    """
    apple_pos = (randint(0, 31), randint(0, 31))
    while apple_pos in [tuple(seg.pos) for seg in snake]:
        apple_pos = (randint(0, 31), randint(0, 31))

    pos = map_grid_to_win(apple_pos, square_size)

    apple = visual.Rect(win, size = square_size,
                        pos = pos, fillColor="red")

    return apple