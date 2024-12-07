import time


def parse_input():

    input_dict = {}

    with open('input/day07.txt') as f:

        for line in f.readlines():

            line = line.rstrip()

            test_value, values = line.split(': ')
            test_value = int(test_value)

            values = [int(x) for x in values.split(' ')]

            input_dict[test_value] = values

    return input_dict


def apply_operator(current_value, next_value, operator):
    if operator == '+':
        return current_value + next_value
    elif operator == '*':
        return current_value * next_value
    elif operator == '|':
        return int(str(current_value) + str(next_value))
    else:
        return next_value
    

def check(test_value, current_value, i, values):

    if i == len(values):
        if current_value == test_value:
            return True
        else:
            return False
    elif current_value > test_value:
        return False
    else:
        cur_value1 = apply_operator(current_value, values[i], '+')
        cur_value2 = apply_operator(current_value, values[i], '*')
        cur_value3 = apply_operator(current_value, values[i], '|')

        check1 = check(test_value, cur_value1, i+1, values)
        check2 = check(test_value, cur_value2, i+1, values)
        check3 = check(test_value, cur_value3, i+1, values)

        return check1 or check2 or check3


def solve(input_dict):

    calibration_result = 0

    for test_value, values in input_dict.items():

        if check(test_value, values[0], 1, values):

            calibration_result += test_value

    return calibration_result


if __name__=="__main__":

    # Parse input
    start = time.time()
    input_dict = parse_input()
    end = time.time()
    print(f"Parse time: {(end-start)*1000} ms")

    # Part 1
    start = time.time()
    print(solve(input_dict))
    end = time.time()
    print(f"Execution time: {(end-start)*1000} ms")
    