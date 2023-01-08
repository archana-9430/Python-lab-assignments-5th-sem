'''3. Write a function which will take input as a list with any kind of
numeric value and give an out as a multiplication of the only integer
values.
For example:
If the given list L1=[1,2,3, ‘Abc’,3.3,4.3, ‘PPP’]
Output will be: 6 i.e., multiplication of 1,2, and 3 '''


def fxn(lst: list):
    ans = 1
    for ele in lst:
        if(type(ele) == int):
            ans *= ele
    return ans



L1 = [1,2,3, "Abc", 3.3, 4.3, "PPP"]
print(fxn(L1))  