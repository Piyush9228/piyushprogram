from sympy import *
var('x,y,z')
f1 = lambda x, y, z: (9 - 2*y - z) / 10
f2 = lambda x, y, z: (-22 - x + z) / 10
f3 = lambda x, y, z: (22 + 2*x - 3*y) / 10
x0=0;y0=0;z0=0
step=1
while(step<=3):
    x1=f1(x0,y0,z0)
    y1=f2(x1,y0,z0)
    z1=f3(x1,y1,z0)
    x0=x1;y0=y1;z0=z1
    step=step+1
print(f"x={round(x1)},y={round(y1)},z={round(z1)}")