'''17. Create a list with ‘n’ no of elements. (no of elements i.e., n and
corresponding elements is to be provided by the user).
Then, print the unique elements of the list.
For example,
If the list: list1 =[1,2,1,1,1,5,6, ‘ppp’, ‘ppp’, ‘abv’]
The output will be:
1,2,5,6, ‘ppp’, ‘abv’ '''


list1 = []
n = int(input("Enter the number of elements: "))

for i in range(0, n):
    ele = (input())
    list1.append(ele)
    
list2 = [list1[0]]
for ele in list1:
    if ele not in list2:
        list2.append(ele)

        
print(list2)
      

