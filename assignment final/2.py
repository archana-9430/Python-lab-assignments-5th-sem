'''2. Write a function which will be able to print an index of list element
without using an index function
'''

def index(lst: list, ele: int):
    for i in range(len(lst)):
        if ele == lst[i]:
            return i

    return -1

    

lst = [1, 2, 3, 4, 5, 6]
print(index(lst, 4)) 