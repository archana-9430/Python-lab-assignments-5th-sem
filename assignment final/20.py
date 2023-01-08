'''20. Write a python code to delete the “name” and “age” key of the
given dictionary.
 sample_dict = {
 "name": "Kelly",
 "age": 25,
 "salary": 8000,
 "city": "New york"
 } '''
 
 
sample_dict = {
 "name": "Kelly",
 "age": 25,
 "salary": 8000,
 "city": "New york"
 }

sample_dict.pop("name")
sample_dict.pop("age")

print(sample_dict)