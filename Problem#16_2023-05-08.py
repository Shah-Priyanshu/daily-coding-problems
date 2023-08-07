""" 
Problem :
You run an e-commerce website and want to record the last N order ids in a log.
Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller 
than or equal to N.
You should be as efficient with time and space as possible.
"""

class OrderLog:
    def __init__(self, N):
        self.N = N
        self.log = [None] * N
        self.count = 0

    def record(self, order_id):
        # Calculate the index where the new order_id should be stored
        index = self.count % self.N

        # Store the order_id in the log
        self.log[index] = order_id

        # Increment the counter
        self.count += 1

    def get_last(self, i):
        if i >= self.N:
            raise ValueError("i should be smaller than N.")

        # Calculate the index of the ith last element
        index = (self.count - i - 1) % self.N

        return self.log[index]

#__main__
N = 5
order_log = OrderLog(N)

order_log.record(1001)
order_log.record(1002)
order_log.record(1003)

print(order_log.get_last(1))  # Output: 1003
print(order_log.get_last(2))  # Output: 1002
print(order_log.get_last(3))  # Output: 1001



