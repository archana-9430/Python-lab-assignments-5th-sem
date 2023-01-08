'''18. Write a code to create two sets ‘a’ and ‘b’. Then compute the
union, intersection of these two sets. Check if ‘a’ is a subset of ‘b’
or not.
Hint: a={1,2,3,4}
 B={1,2} '''
 
 
A = {1,2,3,4}
B = {1,2}

print("Union: ", A | B)
print("Intersection: ", A & B)

if A | B == B: #union == set B
    print("A is a subset of B")
else:
    print("No, A is not a subset of B")

 