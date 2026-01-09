
# Simple Min, Max Finder

import sys


nums = [7, 2, 9, 3, 24, 0, 85, 6, 10, 1, 75, 8, 4, 10]


min_v = sys.maxsize
max_v = -sys.maxsize


for x in nums:

    if min_v > x:
        min_v = x

    if max_v < x:
        max_v = x

        
print(min_v, max_v)