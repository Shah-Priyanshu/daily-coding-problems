""" 
Problem :
The area of a circle is defined as πr^2. 
Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""
import random

class Solution:
    def estimate_pi(num_points):
        points_inside_circle = 0

        for _ in range(num_points):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            if x**2 + y**2 <= 1:
                points_inside_circle += 1

        pi_estimate = 4 * points_inside_circle / num_points
        return pi_estimate

#__main__
num_points = 1000000
estimated_pi = Solution.estimate_pi(num_points)
print(f"Estimated value of π: {estimated_pi:.3f}")

"""The Monte Carlo method is a powerful computational technique that uses random 
sampling to estimate numerical results for complex problems. By generating a large number 
of random samples and simulating the behavior of a system or problem, it provides approximate 
solutions to challenges that might be difficult or impossible to solve analytically. 
The method is widely used in various fields to tackle uncertainty, optimization, and 
simulation tasks, making it an invaluable tool for solving real-world problems."""