# sum of numeric parameters function
def my_function(*args, **kvargs):
    sum = 0
    for arg in args:
        try:
            arg = float(arg)
            sum = sum + arg
        except:
            pass
    for arg in kvargs.keys():
        try:
            arg = float(arg)
            sum = sum + arg
        except:
            pass
    return sum


print(my_function(1, 5, -3, 'abc', [12, 56, 'cad']))
print(my_function())
print(my_function(2, 4, 'abc', param_1=2))


# is value int or not

def is_int():
    value = input("Introduce a value:")
    try:
        value = int(value)
        return 1
    except:
        return 0

if is_int():
    print("Is int")
else:
    print("Is not int")

# recursive
def sum_n(n):
    if isinstance(n,int) == False:
        return -1
    if n==0:
        return 0
    return sum_n(n-1) + n

def sum_n_even(n):
    if isinstance(n,int) == False:
        return -1
    if n==0:
        return 0
    if n%2 == 0:
        return sum_n_even(n-1) + n
    else:
        return sum_n_even(n-1)

def sum_n_odd(n):
    if isinstance(n,int) == False:
        return -1
    if n==0:
        return 0
    if n%2 == 1:
        return sum_n_odd(n-1) + n
    else:
        return sum_n_odd(n-1)

print(sum_n(10))
print(sum_n_even(10))
print(sum_n_odd(10))