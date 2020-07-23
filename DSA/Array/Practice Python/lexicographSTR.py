string=input()
n=int(input())
tempStr=sorted(string)
for i in range(len(tempStr)):
    for j in range(len(tempStr)):
        t=tempStr[i]
        if j+n<=len(tempStr):
            for k in range(j,j+n):
                if i!=k:
                     t+=tempStr[k]
               
        print(t)