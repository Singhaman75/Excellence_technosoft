m=int(input("enter no. of users"))
x,y,a={},{},1
# loop begins
for i in range(0,m):
    b=input("enter user name")
    c=int(input("enter exam score"))
    x.update({a:b})
    y.update({a:c})
    a=a+1
n,a=[],1
for i in range(0,m):
    n.append(y.get(a))
    a=a+1
p=max(n)
answer=list(y.keys())[list(y.values()).index(p)]
print(f"{answer}:{p}")
