import numpy as np


def is_safe(report):

    report = np.array(report)

    diff = np.diff(report)

    if (diff < 0).all() or (diff > 0).all():

        if np.max(np.abs(diff)) <= 3:

            return True
        
    return False


if __name__=="__main__":

    with open('input/day02.txt') as f:

        input = [line.rstrip().split(' ') for line in f.readlines()]
        input = [[int(i) for i in line] for line in input]    

    # Part 1
    safe = 0

    for report in input:

        if is_safe(report):
            safe += 1

    print(safe)

    # Part 2
    safe2 = 0

    for report in input:

        safe_report = False

        for i in range(len(report)):

            dampened_report = [x for j, x in enumerate(report) if j!=i]

            if is_safe(dampened_report):

                safe_report = True
            
        if safe_report:

            safe2 += 1

    print(safe2)