if __name__ == '__main__':
    li=[]
    tli=[]
    max=0
    for _ in range(int(input())):
        name = input()
        score = float(input())
        tli.append(score)
        temp=[name,score]
        li.append(temp)
    sortedli=sorted(tli)
    for i in range(len(sortedli)):
        if sortedli[i]!=sortedli[i+1]:
            max=sortedli[i+1]
            break
    result=[li[i][0] for i in range(len(li)) if li[i][1]==max]
    li=sorted(result)
    for i in range(len(li)):
        print(li[i])