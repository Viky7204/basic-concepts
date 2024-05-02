t = int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x>=y:
       print(y)
    else:
       z=y-x
       r=z*2
    print(r+x)