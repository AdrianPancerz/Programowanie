def poletrapezu(a,b,h):
    if(a>0 and b>0 and h>0):
        return (a+b)*h/2
    else:
        return "złe parametry "

print("Pole trapezu:" ,poletrapezu(5,4,3))