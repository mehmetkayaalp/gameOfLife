from Cell import *

if __name__ == "__main__":
    # Initial statement
    neighbor_array = [0, 0, 0, 0, 0, 0, 0, 0]
    is_alive = 1
    cell = Cell(neighbor_array, is_alive)
    print cell
