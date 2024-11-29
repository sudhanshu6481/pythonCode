if __name__ == '__main__':
    print("Enter the number of commands")
    N = int(input())
    list = []
    for _ in range(N):
        print("Enter the command")

        command=input().split()
        action=command[0]

        if(action=="insert"):

            i= int(command[1])

            e= int(command[2])
            list.insert(i,e)

        elif(action=="print"):
            print(list)

        elif(action=="remove"):

            e= int(command[1])
            list.remove(e)

        elif(action=="append"):

            e = int(command[1])
            list.append(e)

        elif(action=="sort"):
            list.sort()

        elif(action=="pop"):

            i = int(command[1])
            list.pop(i)

        elif(action=="reverse"):
            list.reverse()
