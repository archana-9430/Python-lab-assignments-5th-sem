'''12. Write a program that takes a user’s first name, middle name,
and last name as input in three different variables.
Then - i) Display the abbreviations of the first and middle names
except the last name which is displayed as it is.
For example, if your name is Sunny Bhaveen Chandra, then the output should be S.B.Chandra'''
 
f_name = input("Enter your first name: ")
m_name = input("Enter your middle name: ")
l_name = input("Enter your last name: ")

name = f_name[0] + "." + m_name[0] + "." + l_name
print(name)