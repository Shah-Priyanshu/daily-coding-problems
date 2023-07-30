""" 
Problem :
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. 
Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10,
since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?Given a list of integers, write a function 
that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, 
since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

class Solution:
    def largest_sum_non_adjacent(nums):
        if not nums:
            return 0

        include = nums[0]
        exclude = 0

        for i in range(1, len(nums)):
            new_include = exclude + nums[i]
            exclude = max(include, exclude)
            include = new_include

        return max(include, exclude)

#__main__
print(Solution.largest_sum_non_adjacent([2, 4, 6, 2, 5]))  # Output: 13
print(Solution.largest_sum_non_adjacent([5, 1, 1, 5]))     # Output: 10
