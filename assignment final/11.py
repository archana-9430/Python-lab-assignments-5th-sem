'''11. Check if position 5 to 11 ends with the phrase ‘iNeuron’ in the
string: python text = ‘Welcome to iNeuron , You are a part of
FSDS Bootcamp 2 in iNeuron’ 
Print ‘YES’ if 5 to 11 position of the given string ends with the
phrase ‘iNeuron’, else print ‘NO’ '''

text = "Welcome to iNeuron , You are a part of FSDS Bootcamp 2 in iNeuron"
word = ""
for i in range(5, 12):
    word += text[i]

if(word == "iNeuron"):
    print("YES")
else:
    print("NO")