def my_name(fname):
    print(f"My name is {fname}")

my_name("Shariful")


print("\n-------------------")
def name(h_name, *args):
    print(f"Hey {h_name}")
    for n in args:
        print(f"Nice to meet you, {n}")

name("Tajul", "Tokee", "Akram")


print("\n-------------------")
def t_name(fname,lname):
    print(f"Hello {fname} {lname}")
  
t_name("Shariful", "Islam")


print("\n-------------------")
def my_function(x):
    return x**5

# print(my_function(2))
result = my_function(2)
print(f"Result : {result}")
print("Result : {}".format(result))