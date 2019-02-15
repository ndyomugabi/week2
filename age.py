#!/usr/bin/python3
dob = int (input("enter year of birth"))
age = dob-2019
print("age", age)
if age < 18:
    print("child")
    elif 18 > =  age < 36:
        print("youth")
else:
    age <36
    print("adult")
