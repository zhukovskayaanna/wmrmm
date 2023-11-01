A=5
B=12
C=3
D=8

def e(a,b):
    while b:
        a,b=b,a%b
        return a
def dl(a,b,c,d):
    ch=a*b
    zn=b*c

    p=e(ch,zn)
    ch=ch//p
    zn=zn//p
    return ch,zn
print(dl(A,B,C,D))
