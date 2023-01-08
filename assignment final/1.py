'''1. Write a function which will try to find out length of a string without
using an inbuilt ‘len’ function.
'''

def length(string: str):
    cnt = 0
    while(string[cnt:]):
        cnt += 1
    return cnt

print(length("archana")) 
