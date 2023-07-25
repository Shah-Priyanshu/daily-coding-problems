""" 
Problem :
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
    
Implement car and cdr.


"""


class Solution:
    def cons(a, b):
        """Constructs a pair from two elements.

        Args:
            a (any): The first element of the pair.
            b (any): The second element of the pair.

        Returns:
            function: A pair function that takes another function as an argument.
        """

        def pair(f):
            return f(a, b)
        return pair

    def car(pair):
        """Returns the first element of the pair.

        Args:
            pair (function): A pair function returned by cons.

        Returns:
            any: The first element of the pair.
        """

        def first_element(a, b):
            return a
        return pair(first_element)

    def cdr(pair):
        """Returns the second element of the pair.

        Args:
            pair (function): A pair function returned by cons.

        Returns:
            any: The second element of the pair.
        """

        def second_element(a, b):
            return b
        return pair(second_element)

#__main__
print(Solution.car(Solution.cons(3, 4)))  # Output: 3
print(Solution.cdr(Solution.cons(3, 4)))  # Output: 4
