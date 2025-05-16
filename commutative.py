G={1,2,3,4,5,6}
def f (a,b) :
    return(a*b)%7
for a in G:
    for b in G:
        if f(a,b)!=f(b,a):
            print(" Not commutative")
        break
else:
    print("Commutative")