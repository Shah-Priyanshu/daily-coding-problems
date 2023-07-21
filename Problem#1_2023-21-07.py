""" 
Problem :
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

"""


def solution(lst, k):
    for num in range(len(lst)):
        diff = k - lst[num]
        if diff in lst:
            return True
    return False


# __main__
lst = [int(x) for x in input("Enter the list of numbers separated by spaces: ").split()]
k = int(input("Enter the value of k: "))
#lst = [10, 15, 3, 7]
#k = 17

print(solution(lst, k))
