

# Class:                        	Sorting algorithm

# Worst-case performance	        O(n2)

# Best-case performance	            O(n log n) (simple partition)
# or                                O(n) (three-way partition and equal keys)

# Average performance	            O(n log n)

# Worst-case space complexity	    O(n) auxiliary (naive)
#                                   O(log n) auxiliary

import random


'''
Arguments:
    toSort: list of numbers to sort
    ascending: order to sort, default=True
'''
def quicksort(toSort, ascending=True):
    if [] == toSort or 1 == len(toSort):
        return toSort
    # Random pivot avoids worst case when values are already sorted.
    pivot = random.choice(toSort)
    # Note that temporary lists use significant memory
    # when compared to in-place swapping.
    if ascending:
        left  = [l for l in toSort if l < pivot]
        right = [r for r in toSort if r > pivot]
    else:
        left  = [l for l in toSort if l > pivot]
        right = [r for r in toSort if r < pivot]
    pivot = [p for p in toSort if p == pivot]
    return quicksort(left, ascending) + pivot + quicksort(right, ascending)

def checkIfSorted(check, ascending=True):
    i = 1
    while i < len(check):
        if ascending:
            if check[i-1] > check[i]:
                return False
        else:
            if check[i-1] < check[i]:
                return False
        i += 1
    return True

if __name__ == '__main__':
    numbers = []
    with open('../data/100random.txt', 'r') as file:
        for line in file:
            numbers.append(int(line))

    sorted = quicksort(numbers, False)
    if len(numbers) <= 101:
        for i in range(len(numbers)):
            print(numbers[i], '\t', sorted[i])
    else:
        if checkIfSorted(sorted):
            print('Values sorted.')
        else:
            print('Values not sorted.')
