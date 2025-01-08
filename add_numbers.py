import sys
def add(a,b):
    print("I'm in add function")
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    print("I'm in div function")
    return a/b
def is_even(num):
    if num%2 == 0:
        return True
    else:
        return False
def is_odd(num):
    print("I'm in is_odd function..")
    if num%2 != 0:
        return True
    else:
        return False

arg_one = sys.argv[0]
print(arg_one)