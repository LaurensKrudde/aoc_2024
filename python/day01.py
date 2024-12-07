import numpy as np

input = np.genfromtxt('input/day01.txt').T

first_list, second_list = input[0], input[1]

print(abs(np.sort(first_list) - np.sort(second_list)).sum())

total_similarity = 0

for i in first_list:

    total_similarity += i * (second_list == i).sum()

print(total_similarity)