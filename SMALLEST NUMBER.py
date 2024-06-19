#Smallest Number
a,b,c=list(map(int,input().split()))
if a <b and a<c:
    print("smallest number",a)
elif b<a and b<c:
    print("smallest number",b)
else:
    print("smallest number",c)
