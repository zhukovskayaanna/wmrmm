
def f(n):
    for i in range(1,n+1):
        if 2**i<=n:
            m=i
    print("показатель степени:",m)
    print("Степень:",2**m)




n=int(input("ВВедите число:"))
f(n)

