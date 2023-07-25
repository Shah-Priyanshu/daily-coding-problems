""" 
Problem :
Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""


class Solution:
    def first_missing_positive(lst):
        """Summary

        Args:
            lst (list): list of numbers

        Returns:
            i+1 : integer, the lowest positive integer
        """
        n = len(lst)
        for i in range(n):
            while 1 <= lst[i] <= n and lst[lst[i] - 1] != lst[i]:
                # Swap lst[i] with the element at its correct position
                lst[lst[i] - 1], lst[i] = lst[i], lst[lst[i] - 1]
        # Iterate through the sorted array to find the first missing positive integer
        for i in range(n):
            if lst[i] != i + 1:
                return i + 1

        # If all positive integers from 1 to n are present, the missing integer is n + 1
        return n + 1


# __main__
lst = [int(x) for x in input("Enter the list of numbers separated by comma: ").split(',')]
# lst = [3, 4, -1, 1]

print(Solution.first_missing_positive(lst))
