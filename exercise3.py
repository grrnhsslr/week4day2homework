# Convert the list below from Celsius to Farhenheit, using the map function with a lambda...
#
# Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angeles', 111.2), ('Miami', 84.2)]

# F = (9/5)*C + 32
places = [('Nashua', 32), ("Boston", 12), ("Los Angeles", 44), ("Miami", 29)]

# def tempfix():
#     for temp in places:
#         if temp[1]:
#             new_temp = (9/5)*temp[1] + 32
#             return temp[0], new_temp
#             places.remove(temp[1])
#             places.append(new_temp)

print(list(map(lambda x: (x[0], (9/5)*x[1]+32), places)))
