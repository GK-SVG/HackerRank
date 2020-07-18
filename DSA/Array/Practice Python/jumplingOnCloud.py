def jumpingOnClouds(c):
    count=[]
    i=0
    c.append(1)
    c.append(1)
    while(i<(len(c)-2)):
        if c[i+2]!=1 and i+2 not in count:
            count.append(i+2)
            i+=2
        elif c[i+1]!=1 and i+1 not in count:
            count.append(i+1)
            i+=1
        else:
            i+=1
    return len(count)


if __name__ == '__main__':
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    print(result)
    