# fruits = ['apple','peaches','blueberrys',1,True]
# print(fruits[1])
# print(fruits[-1])
# print(fruits[1:4])
# print(fruits[:4])
# print(fruits[2:])

# print("\n----------")
# fruits[3] = "banana" # change index 3
# print(fruits)
# fruits.insert(4,"watermelon") # new 4 index will be insert
# print(fruits)
# fruits.append("cherry")  #insert in the last position
# print(fruits)

# print("\n---------------------")
# fruits2 = ['mangoes','pineapple']
# fruits.extend(fruits2)
# print(fruits)

# print("\n---------------------")
# fruits.remove("cherry")
# print(fruits)
# # fruits.pop(1)
# print(fruits)


print("\n---------------------")
fruits = ['apple','peaches','blueberrys','pineapple']
# fruits.sort(reverse=False)
# fruits2 = [expression for item in iterable if condition]
fruits2 = [f for f in fruits if f!="apple"]
print(fruits2)