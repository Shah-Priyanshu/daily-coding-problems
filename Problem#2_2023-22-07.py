"""
Given an array of integers, return a new array such that each element at index i of the new array 
is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

class Solution:
    def ArrayProduct(lst):
        """Summary

        Args:
            lst (list): list of numbers

        Returns:
            new_lst (list): list of numbers
        """
        new_lst = []
        for i in lst:
            prod = 1
            for j in lst:
                if j != i:
                    prod *= j
            new_lst.append(prod)
        return(new_lst)

#__main__
lst = [int(x) for x in input("Enter the list of numbers separated by comma: ").split(',')]
# lst = [1, 2, 3, 4, 5]
print(Solution.ArrayProduct(lst))