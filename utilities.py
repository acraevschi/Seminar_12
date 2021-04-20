
def map_grid_to_win(ipos, square_size=(2/30, 2/30)):
    """
    Returns x and y position on the grid
    """

    x_pos = -1 + (ipos[0] * square_size[0]) + square_size[0]/2
    y_pos = 1 - (ipos[1] * square_size[1]) - square_size[1]/2

    return (x_pos, y_pos)

def inverse_map_grid(float_pos, square_size=(2/30, 2/30)):
    """
    Returns current position in index value, given the
    current position in PsychoPy "norm" units.
    """
    float_pos = tuple(float_pos)
    x_pos = (float_pos[0] + 1 - (square_size[0]/2))/square_size[0]
    y_pos = (float_pos[1] - 1 + (square_size[1]/2))/square_size[1]
    x_pos = round(x_pos)
    y_pos = round(y_pos)

    return (x_pos, y_pos)