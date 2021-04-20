from psychopy import visual, event
from utilities import map_grid_to_win
from snake import create_snake, add_segment, draw_snake
from apple import create_apple
import move_snake

GRID_SIZE = (30, 30)
SQUARE_SIZE_PIX = 20
SQUARE_SIZE = (2/GRID_SIZE[0], 2/GRID_SIZE[1])

win = visual.Window(size=(GRID_SIZE[0]*SQUARE_SIZE_PIX,
                    GRID_SIZE[1]*SQUARE_SIZE_PIX), units="norm")

game_over = False
snake = create_snake(win, SQUARE_SIZE)
apple = create_apple(win, SQUARE_SIZE, snake)
i_pos = (0, 0)

while not game_over:
    draw_snake(win, snake)

    if event.getKeys(keyList=["up"]):
        move_snake.move_up(snake)
        draw_snake(win, snake)
    if event.getKeys(keyList=["down"]):
        move_snake.move_down(snake)
        draw_snake(win, snake)
    if event.getKeys(keyList=["left"]):
        move_snake.move_left(snake)
        draw_snake(win, snake)
    if event.getKeys(keyList=["right"]):
        move_snake.move_right(snake)
        draw_snake(win, snake)
    if event.getKeys(keyList=["escape"]):
        game_over = True

win.close()

