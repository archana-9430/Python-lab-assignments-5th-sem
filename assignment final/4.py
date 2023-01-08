'''4. Find the largest number from the given list:
 numbers= [12,75,150,180,145,525,50] '''
 
 
def fxn(numbers: list):
    mx = numbers[0]
    for ele in numbers:
        mx = max(mx, ele)
    return mx

 
numbers = [12,75,150,180,145,525,50]
print(fxn(numbers))  #525