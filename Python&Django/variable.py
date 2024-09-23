# def sum(a,b):
#     return (a+b)

# a = int(input('Enter the value of a : '))
# b = int(input('Enter the value of b : '))

# print(f'Sum of {a} and {b} is {sum(a,b)}')


# name = "Shariful Islam"
# a = "4"
# print(name)
# print(type(a))


# x = "I'm exusted.."

# def func1():
#     x = "I'm starved..."
#     print(x)

# print(x)
# func1()
# print(x)


x = "I'm exusted.."

def func1():
    global x
    x = "I'm starved..."

print(x)
func1()
print(x)