from collections import defaultdict
import numpy as np
import itertools


def parse_input():

    antennas = defaultdict(list)

    with open('input/day08.txt') as f:

        for i, line in enumerate(f.readlines()):

            line = line.rstrip()

            for j, ch in enumerate(line):
                if ch.isdigit() or ch.isalpha():
                    antennas[ch].append(np.array([i, j]))
            
    return antennas, i + 1, j + 1


class AntennaPark:

    def __init__(self, antennas, boundary_i, boundary_j):

        self.antenna_loc_dict = antennas
        self.boundary_i = boundary_i
        self.boundary_j = boundary_j

    def part1(self):

        antinodes = set()

        for antenna in self.antenna_loc_dict.keys():

            antenna_combinations = list(itertools.combinations(self.antenna_loc_dict[antenna], 2))

            for an1, an2 in antenna_combinations:

                anti1, anti2 = self.antinodes_pair(an1, an2)

                if self.within_boundary(anti1):
                    antinodes.add(tuple(anti1))
                if self.within_boundary(anti2):
                    antinodes.add(tuple(anti2))

        return len(antinodes)
    
    def part2(self):

        antinodes = set()

        for antenna in self.antenna_loc_dict.keys():

            antenna_combinations = list(itertools.combinations(self.antenna_loc_dict[antenna], 2))

            for an1, an2 in antenna_combinations:

                antinodes_for_antenna_pair = self.all_antinodes_for_antenna_pair(an1, an2)

                antinodes = antinodes.union(antinodes_for_antenna_pair)

            for location in self.antenna_loc_dict[antenna]:

                antinodes.add(tuple(location))

        return len(antinodes)

    def antinodes_pair(self, antenna1, antenna2):

        diff = antenna1 - antenna2

        return antenna1 + diff, antenna2 - diff

    def all_antinodes_for_antenna_pair(self, antenna1, antenna2):

        set_antinodes = set()

        diff = antenna1 - antenna2

        n = 1
        while self.within_boundary(antenna1 + n * diff):

            set_antinodes.add(tuple(antenna1 + n * diff))
            n += 1

        m = 1
        while self.within_boundary(antenna2 - m * diff):

            set_antinodes.add(tuple(antenna2 - m * diff))
            m += 1

        return set_antinodes

    def within_boundary(self, antinode):

        return 0 <= antinode[0] < self.boundary_i and 0 <= antinode[1] < self.boundary_j



if __name__=="__main__":

    antennas, boundary_i, boundary_j = parse_input()

    park = AntennaPark(antennas, boundary_i, boundary_j)

    print(park.part1())
    print(park.part2())
