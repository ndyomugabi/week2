
y = input("Enter a string: ")
# for z in y:
#     if z in x:
#         print(z)


def string_vowel(string_input):
        store_list = []
        x = ['a','e','i','o','u']
        repeated_vowels = []
        nonreapted_vowels=[]
        alphabt="abcdefghijklmnopqrstuvwxyz"
        reaptions=0
        for s in string_input:
                if s in x:
                        store_list.append(s)
        for m in x:
                vowel_count = store_list.count(m)
                if vowel_count > 1:
                        repeated_vowels.append(m)
                elif vowel_count == 1:
                        nonreapted_vowels.append(m)
        for val in alphabt:
                count= string_input.count(val)
                if count > 1:
                        reaptions= reaptions+1
                        
        final_vowels= nonreapted_vowels + repeated_vowels
        print((''.join(final_vowels), reaptions))

string_vowel(y)
                        


