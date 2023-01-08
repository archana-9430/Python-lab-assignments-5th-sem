'''16. Find the number of vowels present in a given string.
 The string is to be provided by the user as input. '''
 
 
string = input("Enter a string: ")
vowels = ['a', 'e', 'i', 'o', 'u']
vowels_cnt = 0
for char in string:
    if char in vowels:
        vowels_cnt += 1
        
print(vowels_cnt)
 