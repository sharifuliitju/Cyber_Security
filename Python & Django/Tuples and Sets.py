# tuple1 = ("apple", 1, 1.5, True)
# print(tuple1)
# print(len(tuple1))
# print(tuple1[0])
# print(tuple1)


print("\n---------------")
print("-----Set------")
set1 = {"apple","cherry","orange","apple"} #only one apple will be print
print(set1) 
print(len(set1))
# print(set1[0]) #unsupported
for f in set1:
    print(f)

set1.add("kiwi")
# set1.remove("cherry")
set1.pop() #pop in random
print(set1)