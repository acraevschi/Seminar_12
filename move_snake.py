from psychopy import visual, event
from utilities import map_grid_to_win, inverse_map_grid
from snake import add_segment, draw_snake

def move_left(snake):
    current_pos = inverse_map_grid(snake[0].pos)
    new_pos = (current_pos[0] - 1, current_pos[1])
    snake[-1].pos = map_grid_to_win(new_pos)

    return snake

def move_right(snake):
    current_pos = inverse_map_grid(snake[0].pos)
    new_pos = (current_pos[0] + 1, current_pos[1])
    snake[-1].pos = map_grid_to_win(new_pos)

    return snake

def move_up(snake):
    current_pos = inverse_map_grid(snake[0].pos)
    new_pos = (current_pos[0], current_pos[1] + 1)
    snake[-1].pos = map_grid_to_win(new_pos)

    return snake

def move_down(snake):
    current_pos = inverse_map_grid(snake[0].pos)
    new_pos = (current_pos[0], current_pos[1] - 1)
    snake[-1].pos = map_grid_to_win(new_pos)

    return snake

####################################
## Need to finish the function below

# def eat_apple(win, snake, apple):
#     for segment in snake:
#         if segment.pos == apple.pos:
#             add_segment(win, snake, )