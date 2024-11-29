def sum(a,b):
    add= a+b
    return add

def string_reverse(S):
    a=S[::-1]
    return a
print("Enter the number")
a= int(input())
b= int(input())
print(sum(a,b))
print("Enter the String")
S=input()
print(string_reverse(S))