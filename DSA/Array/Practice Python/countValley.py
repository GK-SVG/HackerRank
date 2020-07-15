def countingValleys(n, s):
    count=0
    count2=0
    for i in range(len(s)):
        if s[i]=='U':
            count+=1
            if count==0:
               count2+=1
        elif s[i]=='D':
            count-=1
    return count2



if __name__ == '__main__':
    n = int(input())
    s = input()
    result = countingValleys(n, s)
    print(result)