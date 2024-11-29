def if_fizzBuzz():
    for i in range(100):
        if i%3==0:
            if i % 3 == 0 and i % 5 == 0:
                print(str(i) + " " + "FizzBuzz")
            else:
                print(str(i)+" "+"Fizz")
        elif i%5==0:
            if i % 3 == 0 and i % 5 == 0:
                print(str(i) + " " + "FizzBuzz")
            else:
                print(str(i)+" "+"Buzz")

if_fizzBuzz()