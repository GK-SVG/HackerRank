n=int(input())
p=int(input())
if p<(int(n/2)+1):
    count=1
    Pcount=0
    while count<p:
        count+=2
        Pcount+=1
else:
    if n%2==0:
        Pcount=0
        while n>p:
            n-=2
            Pcount+=1
    else:
        Pcount=-1
        while n>p:
            n-=2
            Pcount+=1   
print(Pcount)


