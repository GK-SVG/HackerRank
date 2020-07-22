# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#     li=[]
#     for i in range(x+1):
#         for j in range(y+1):
#             for k in range(z+1):
#                 templi=[i,j,k]
#                 li.append(templi)
#     sumli=[li[i] for i in range(len(li)) if sum(li[i])!=n]
#     print(sumli)

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print ([[i,j,k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n])