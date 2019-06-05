str,l=input(),[]
x=[l.append(i) for i in str]
for i in range(0,len(l),2):
    l[i],l[i+1]=l[i+1],l[i]
print("".join(l))
