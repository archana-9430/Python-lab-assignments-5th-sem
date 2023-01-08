'''10. Count the number of times iNeuron appears in the string.
python text = ‘Welcome to iNeuron , You are a part of FSDS Bootcamp 2 in iNeuron .
I hope you are enjoying the course by iNeuron’ 
'''

text = "Welcome to iNeuron , You are a part of FSDS Bootcamp 2 in iNeuron . I hope you are enjoying the course by iNeuron"
word = "iNeuron"

words = text.split()
count = 0
for string in words:
    if string == word:
        count += 1
        
print(count)


