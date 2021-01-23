def add(a):
    b,c=0,len(a)
    for i in range (0,c):
        b=b+a[i]
    return b

x=[int(i) for i in input().split(' ')]
print(add(x))
