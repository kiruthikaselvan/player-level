ele=int(input())
f=1
if ele==0:
    print("1")
else:
    for i in range(1,ele+1):
        f=f*i
    print(f)
