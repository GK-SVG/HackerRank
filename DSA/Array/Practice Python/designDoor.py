# Enter your code here. Read input from STDIN. Print output to STDOUT
N,M=map(int, input().split())
s1='.|.'
num=1
for i in range(int(N/2)):
    print((s1*num).center(M,'-'))
    num+=2
num-=2
print('WELCOME'.center(M,'-'))
for i in range(int(N/2)):
    print((s1*num).center(M,'-'))
    num-=2

