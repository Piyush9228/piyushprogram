from sympy import*
f=lambda x:x**3-4*x-9
a=2
b=3
step=1
while(step<=3):
    x=(a+b)/2
    print(f"itr={step},x={x},f(x)={round(f(x),3)}")
    if f(a)*f(x)<0:
        b=x
    else:
        a=x
    step=step+1
print("Approx root is=",x)
