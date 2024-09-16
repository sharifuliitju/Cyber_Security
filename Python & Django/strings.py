x = 'Shariful Islam'
y = """Hello How are you
I'm fine
what about you"""

print(x)
print(y)

print("\n---------")
print(x[0])
print(x[2:5])
print(x[:])

print("\n---------")
print(len(x))
print(len(y))


print("\n---------")
a = "Shariful"
b = "Islam"
age = 26
c = f'{a} {b}'
d = "{} {}".format(a, b)  #same as c
e = "{} {} is {} year's old.".format(a,b,age)

print(a+b)
print(c)
print(d)
print(e)
print(a.lower())
print(a.isdigit())


print("\n---------")
f = "24.43"
print(f.isdigit())
print(f.isnumeric())


