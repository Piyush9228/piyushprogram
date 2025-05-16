from sympy import*
x=[1,2,3,4]
y=[1,8,27,64]
X=2.5;h=1;s=y[0];term=1;k=1;n=1;n=len(x)
p=(X-x[0])/h
print("difference table")
print(*x,sep="\t")
print(*y,sep="\t")
for i in range(0,n-1):
    z=[]
    for j in range(0,n-i-1):
        y[j]=y[j+1]-y[j]
        z.append(y[j])
    print(*z,sep="\t")
    term=term*(p-i)/k
    k=k+1
    s=s+term*y[0]
print("y(2.5)=",round(s,3))

