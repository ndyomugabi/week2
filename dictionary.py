# dob = int(input("enter dob"))
# python
d = {}
for x in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
    sq = x*x
    d[x]=sq
# print (d)

new_dict = {}


# def square(list_in):
#     for i in list_in:
#         sqre = i*i
#         new_dict[i] = sqre

# nos = [2,3,4]

# square(nos)
# print(new_dict)

def square(start, stop):
    for i in range(start,stop):
        sqre = i*i
        new_dict[i] = sqre

square(1,15)

print(new_dict)
    


