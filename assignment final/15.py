'''15. Write a python code:
 i) create a file named “test.txt” in the working directory
 ii)Open the file in ‘w’ mode and write your name and
 department in the file.
 iii) Close the file.
 iv) Display the content of the file. '''

#1
obj = open("test.txt", "x")   
#2
obj = open("test.txt", "w")
obj.write("Archana Kumari, IRPE (BTech ECE)")
#3
obj.close()
#4
f1 = open("test.txt", "r")
txt = f1.read()
print(txt)

