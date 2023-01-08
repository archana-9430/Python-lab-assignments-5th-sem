'''8. Write a user defined function which can calculate the sum of all
numbers from 1 to a given number n. '''

def calc_sum(n: int):
    sum_all = 0
    for i in range(1, n + 1):
        sum_all += i
    return sum_all
