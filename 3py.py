from sympy import*
var('x,y')
f=lambda x:1/(1+x**2)
x0=0;xn=6;n=6;h=1
sol=f(0)+f(6)
for i in range(1,n):
    sol=sol+2*f(i*h)
sol=round(h/2*sol,4)
pprint(sol)

