#farhest coordinate
a=list(map(int,input().split()))
max=-1
s=0
for i in a:
    s=s+i
    if s>max:
        max=s
print(max)
