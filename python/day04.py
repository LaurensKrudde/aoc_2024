def search(grid):
    """ Loop over the grid coordinates and search at an 'X' for part 1 and at an 'A' for part 2. """

    ans = 0
    ans2 = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):

            # Search for 'XMAS'
            if grid[x][y] == 'X':
                ans += search_at_X(grid, x, y)

            # Search for X-'MAS'
            if grid[x][y] == 'A':
                ans2 += search_at_A(grid, x, y)

    return ans, ans2


def search_at_X(grid, x, y):
    """ Search in every direction for the word 'XMAS'. """

    word = 'XMAS'

    # Directions to search in
    dir = [(0,1), (1,0), (0,-1), (-1, 0), (1,1), (1,-1), (-1,1), (-1,-1)]

    # Keep track of feasible search directions
    search_dirs = dir.copy()

    # Expand search to next letter of word
    for k in range(1, len(word)):

        # Check all directions for the next letter
        for (i, j) in dir:

            # Skip if infeasible direction
            if (i, j) not in search_dirs:
                continue
            
            # Next letter location
            x1, y1 = x + k*i, y + k*j

            if check_boundary(grid, x1, y1):

                # Stop searching in direction if wrong letter observed
                if grid[x1][y1] != word[k]:
                    search_dirs.remove((i, j))

            # Stop searching in direction if boundary overstepped
            else:
                search_dirs.remove((i, j))

    # Remaining directions found the full word 'XMAS'
    return len(search_dirs)


def search_at_A(grid, x, y):
    """ Look at the 4 letters in an X around the letter 'A'. """

    # X (diagonal) directions
    dir = [(1,1), (1,-1), (-1,1), (-1,-1)]

    letters = []

    for (i, j) in dir:
        
        x1, y1 = x + i, y + j

        if check_boundary(grid, x1, y1):

            letters += [grid[x1][y1]]

    # We found an X-MAS if there are two M's and two S's such that the opposite letters are unequal (otherwise we have SAS and MAM)
    if len(letters) == 4 and letters.count('M') == 2 and letters.count('S') == 2 and (letters[0] != letters[3]) and (letters[1] !=  letters[2]):
        return 1
    else: 
        return 0


def check_boundary(grid, x, y):
    """ Check if the x,y coordinates are within the grid. """
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


if __name__=="__main__":

    with open('input/day04.txt') as f:

        input = [list(line.rstrip()) for line in f.readlines()]

    print(search(input))
    