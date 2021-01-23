a=[0,0,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,1,0,0]
x=0
m=0
for i in range(len(a)):
    if a[i]==1:
        for j in range(i,len(a)):
            if (a[j]!=0):
                m=m+1
                if m>x:
                    x=m
            else:
                    m=0

print(x)  

