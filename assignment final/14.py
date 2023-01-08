'''14. Write a python code to print given pattern using loop.
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5 
'''

i, j = 5, 1

while i > 0:
    for i in range(i):
        print(j, end = " ")
    print()
    j += 1
i -= 1
