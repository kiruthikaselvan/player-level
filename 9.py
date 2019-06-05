l,u=map(int,input().split())
pc=0
for i in range(l,u+1):
    c=0
    for j in range(1,i+1):
        if(i%j==0):
            c=c+1
    if c==2:
        pc=pc+1
print(pc)
