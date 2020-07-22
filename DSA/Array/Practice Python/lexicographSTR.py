string=input()
n=int(input())
tempStr=sorted(string)
for i in range(len(tempStr)):
    for j in range(len(tempStr)-n+1):
        t=tempStr[i]
        for k in range(j,j+n):
            if i!=k:
                t+=tempStr[k]
        if len(t)==n:
            print(t)
            