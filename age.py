#!/usr/bin/python3
dob = int(input("Enter year of birth: "))
age = 2019-dob
def agecalc(age_input):
    print(age_input)
    if age_input < 18:
        print("minor")
    elif age_input >= 18 and age_input <= 36:
        print("youth")
    else:
        
        print("elder")

agecalc(age)
    
