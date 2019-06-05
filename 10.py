e1,e2=input().split()
c=0
for i in range(0,len(e1)):
    if e1[i]!=e2[i]:
        c=c+1
        if c>1:
            print("no")
            break
else:
    print("yes")
    
        
