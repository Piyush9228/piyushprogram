from sympy import*
var('k,x')
y=Function('y')
f=Function('f')
f=lambda y,x:diff(y(x),x)+x**2*diff(y(x),x)**2
e=diff(f(y,x),diff(y(x),x))-k
sol=dsolve(e)
pprint(sol)
