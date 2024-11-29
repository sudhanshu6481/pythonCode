def if_adult(age):
    if age>18:
        print("you are an adult")
    elif age<18:
        print("you are minor")

print("enter your age")
age=int(input())
if_adult(age)