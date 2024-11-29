def isPalindrom(s):
    x= s[::-1]

    if(s==x):
        print("Palindrom")
    else:
        print("Symetrical")

s='geeg'
isPalindrom(s)