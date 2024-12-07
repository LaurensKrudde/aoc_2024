import re
from collections import defaultdict


def correct_order(page_numbers, order_rules):

    for i, page_number in enumerate(page_numbers):

        if len(set.intersection(set(page_numbers[:i]), set(order_rules[page_number]))) != 0:
            
            return False
        
    return True


if __name__=="__main__":

    with open('input/day05.txt') as f:

        order_rules = defaultdict(list)
        updates = []

        reading_orders = True

        for line in f.readlines():

            line = line.rstrip()

            if line == '':
                reading_orders = False
                continue

            if reading_orders:  
                x, y = [int(k) for k in re.findall('\d+', line)]
                order_rules[x].append(y)

            else:
                update = [int(k) for k in line.split(',')]
                updates.append(update)

    # Part 1
    ans = 0
    for page_numbers in updates:
                
        if correct_order(page_numbers, order_rules):
            
            middle = int((len(page_numbers)-1)/2)
            ans += page_numbers[middle]
    
    print(ans)

    # Part 2 (assumes all order rules are explicitly given, which turns out to be the case)
    ans2 = 0
    for page_numbers in updates:

        if not correct_order(page_numbers, order_rules):

            sorted_page_numbers = [0]*len(page_numbers)

            for page_number in page_numbers:

                # The number of pages after this page are the pages that occur in both the order_rules and the page_numbers
                numbers_after = len(set.intersection(set(order_rules[page_number]), set(page_numbers)))

                # Then we know the position of the current page
                sorted_page_numbers[len(page_numbers)-1-numbers_after] = page_number

            ans2 += sorted_page_numbers[int((len(page_numbers)-1)/2)]
    
    print(ans2)
