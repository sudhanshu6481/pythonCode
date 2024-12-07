def is_Prime(n):

    if n in [2,3]:
        return True
    elif n==1 or n%2==0:
        return False
    else:
        return True

def is_Palidrom(n=56): #Default argument if no parameter is provided
    rev=0
    number=n
    while n!=0:
        temp=n%10
        rev=rev*10+temp
        n//=10
    if rev==number:
        return True
    else:
        return False

def student(firstname, lastname): #Key arguments
    print('Student name is '+firstname+' '+lastname)

def positionalArguments(name, times):
    for greetings in range(times):
        print(f'Good morning {name}')

def arbitraryNonKeyArgs(*args):
    """function to print arbitrary non key word args"""
    for arg in args:
        print(arg)

def arbitraryKeyArgs(**kwargs):
    """function to print arbitrary key word args"""
    for key, value in kwargs.items():
        print("%s = %s" % (key, value))

cube = lambda x: x*x*x #Anonymous function

def factorial(n): #recursive function
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
n=66
print(is_Prime(n))
print(is_Palidrom(n))
print('Default output when default param is provided: '+'\n'+str(is_Palidrom()))
student(lastname='Gupta',firstname='Sudhanshu')
positionalArguments('Sudhanshu',times=5)
arbitraryNonKeyArgs('hello','world')
print(arbitraryNonKeyArgs.__doc__)
arbitraryKeyArgs(lastname='Gupta',firstname='Sudhanshu')
print(cube(3))
print(factorial(5))