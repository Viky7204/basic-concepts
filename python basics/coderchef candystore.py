t=int(input())
for i in range(t):
    num=input()
    sum=0
    l=len(num)
    for j in range(l):
        sum+=int(num)%10
        num=int(num)/10
print(sum)