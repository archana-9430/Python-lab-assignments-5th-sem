'''6. Write a programme to display only those number from a list that satisfy the conditions:
 i) The number is divisible by 5
 ii) If the number is garter than 150, then skip it and move to the next num
 iii) if the number is greater than 500, then stop the loop
Given list is: numbers=[12,75,150,180,145,525,50]'''


def fxn(numbers: list):
    for ele in numbers:
        if ele > 500: 
            break
        elif ele > 150:
            continue
        elif ele % 5 == 0:
            print(ele, end = " ")

numbers = [12,75,150,180,145,525,50]
fxn(numbers)  