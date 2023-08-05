""" 
Problem :
Given a stream of elements too large to store in memory, 
pick a random element from the stream with uniform probability.
"""
import random
class Solution:
    def reservoir_sampling(stream):
        sample = None
        count = 0
        
        for element in stream:
            count += 1
            if random.randint(1, count) == 1:
                sample = element
        
        return sample


#__main__
stream = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random_element = Solution.reservoir_sampling(stream)
print("Random element from the stream:", random_element)