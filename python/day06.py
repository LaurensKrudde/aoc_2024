import copy
import numpy as np


DIRS = np.array([[-1, 0], [0,1], [1,0], [0,-1]])


def walk(map, start_coords, dir_idx=0):
    
    traversed = []
    possible_obstructions = set()
    cur_dir = dir_idx
    coords = start_coords

    i = 0
    while True:

        traversed.append(tuple(coords) + (cur_dir,))

        next_coords = coords + DIRS[cur_dir]

        # Leave map
        if not boundary_check(map, next_coords):
            break
        
        # Turn right
        elif map[tuple(next_coords)] == '#' or map[tuple(next_coords)] == 'O':
            cur_dir = (cur_dir + 1) % 4
        
        # Move forward
        else:

            # Create obstruction at next tile
            if not (next_coords == start_coords).all():
                tile_before_obstruction = map[tuple(next_coords)]
                map[tuple(next_coords)] = 'O'

                # Check if it results in loop
                if check_loop(map, start_coords):
                    possible_obstructions.add(tuple(next_coords))

                # Restore tile
                map[tuple(next_coords)] = tile_before_obstruction

            coords = next_coords
        
        i += 1

    part1 = len(set((x, y) for x, y, _ in traversed))
    part2 = len(possible_obstructions)

    return part1, part2


def check_loop(map, start_coords, dir_idx=0):

    traversed = set()
    cur_dir = dir_idx
    coords = start_coords

    while True:

        traversed.add(tuple(coords) + (cur_dir,))

        next_coords = coords + DIRS[cur_dir]

        if not boundary_check(map, next_coords):
            break
        
        elif map[tuple(next_coords)] == '#' or map[tuple(next_coords)] == 'O':
            cur_dir = (cur_dir + 1) % 4
        
        else:
            coords = next_coords

        if (tuple(coords) + (cur_dir,)) in traversed:
            return True

    return False


def print_map(map):

    for row in map:
        print(''.join(row))

    
def boundary_check(map, coords):

    return 0 <= coords[0] < len(map) and 0 <= coords[1] < len(map[0])


def find_start(map):

    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '^':
                return np.array([i, j])


if __name__=="__main__":

    with open('input/day06.txt') as f:

        map = [list(line.rstrip()) for line in f.readlines()]
        map = np.array(map)

    start_coords = find_start(map)
    print(walk(map, start_coords))
