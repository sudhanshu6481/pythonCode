def reverseWords(s):

    x=s.split()[::-1]
    l=[]
    for i in x:
        l.append(i)

    print(" ".join(l))

def removeIthChar(n,s):
    if n==0:
        x=s[1:]
        print(x)
    elif n==len(s):
        x=s[:n]
        print(x)
    else:
        x=s[:n]+s[n+1:]
        print(x)

def stringLength(s):
    counter=0
    for i in s:
        counter= counter+1;

    print(counter)

def countSpaces(s):
    res= sum(not chr.isspace() for chr in s)
    print("characters without space: ",res)

def evenLengthWords(s):
    x=s.split()
    for i in x:
        if len(i)%2==0:
            print(i)

def uperCaseHalfString(s):
    n=len(s)/2
    string=s[int(n):]
    print(string.upper())

s="I love python"
uperCaseHalfString(s)
evenLengthWords(s)
print(s)
print("length of String is: ", len(s))
reverseWords(s)
removeIthChar(4,s)
stringLength(s)
countSpaces(s)