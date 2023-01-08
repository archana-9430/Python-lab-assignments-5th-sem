'''5. Print all the i) even numbers, ii) prime numbers in between 100-999 '''

#%% 1. even numbers

for num in range(100, 1000):
    if num % 2 == 0:
        print(num, end = " ")
print()
        
#%% 2. prime numbers
for num in range(100, 1000):
    count = 0
    for i in range(2, int(num**1/2)):
        if(num % i == 0):
            count = count + 1
            break

    if (count == 0 and num != 1):
        print(" %d" %num, end = ' ')
        
        
