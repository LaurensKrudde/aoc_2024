import re


if __name__=="__main__":

    with open('input/day03.txt') as f:

        input = ''.join(f.readlines())

    # Part 1
    instructions = re.findall("mul\(\d+,\d+\)", input)

    result = 0
    
    for instr in instructions:

        x, y = re.findall("\d+", instr)

        result += int(x) * int(y)

    print(result)

    # Part 2
    instructions2 = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", input)

    result2 = 0

    active = True

    for instr in instructions2:

        if instr == "do()":
            active = True
        elif instr == "don't()":
            active = False
        elif active:
            x, y = re.findall("\d+", instr)
            result2 += int(x) * int(y)

    print(result2)

