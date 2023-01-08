'''19. Write a python code to create a dictionary with four keys (use the following given key names).
First key : “Student_1 Name”
Second key: “ Studen_1 Numbers”
Third key: “Student_2 Name”
Fourth key: “Student_2 Numbers”
- First and Third key values are the name of two students. Second
and fourth key values should be a LIST consisting of the obtained
marks (out of 100) of three subjects. (Name of user should be
provided by the user)
- print the student name and his/her obtained average marks by
using the dictionary’s key values.
Hint: name1=input(“student 1 name:”)
 Numbers=[80,90]
Use name1 as the key and Numbers as the value of the key. '''


n1 = input("Student 1 name: ")
n2 = input("Student 2 name: ")

Nos1 = [95, 80, 90]
Nos2 = [70, 99, 63]

sum1, sum2 = 0, 0
for ele in Nos1:
    sum1 += ele

for ele in Nos2:
    sum2 += ele

avg1 = sum1 / len(Nos1)
avg2 = sum2 / len(Nos2)

D = dict([(n1, Nos1), (n2, Nos2)])
print(D)
# Dict = { "Student_1 Name": n1, " Studen_1 Numbers": Nos1, "Student_2 Name": n2, "Student_2 Numbers": Nos2}
print("Student_1 name is: ", n1, ". His average marks is: ", avg1)
print("Student_2 name is: ", n2, ". His average marks is: ", avg2)
