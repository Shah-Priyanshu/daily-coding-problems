""" 
Problem :
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""
import time
class Solution:
    def job_scheduler(f, n):
        """_summary_

        Args:
            f (function): The function you want to delay
            n (int): milliseconds
        """
        # Convert milliseconds to seconds for the time.sleep() function
        seconds = n / 1000.0
        
        # Sleep for the specified time before calling the function
        time.sleep(seconds)
        
        # Call the function after the specified time has elapsed
        f()

# Example function to be called by the job scheduler
def example_function():
    print("The job scheduler called this function after the specified time.")

# Example usage of the job scheduler
milliseconds_delay = 5000  # 5 seconds
Solution.job_scheduler(example_function, milliseconds_delay)
