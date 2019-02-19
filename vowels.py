
y = input("Enter a string: ")
# for z in y:
#     if z in x:
#         print(z)


def string_vowel(string_input):
        store_list = []
        x = ['a','e','i','o','u']
        for s in string_input:
                if s in x:
                        store_list.append(s)

        print((store_list, len(store_list)))

string_vowel(y)
                        


