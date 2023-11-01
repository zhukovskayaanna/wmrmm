
def f(n):
    for i in range(2,n+1):
        if n%i==0:
            print(i)
            break



n=int(input("ВВедите число:"))
f(n)

