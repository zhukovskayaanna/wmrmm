def f(n):
    k=0
    g=-1
    m=0
    while n!=0:
        if g==n :
            k+=1
        else:
            g=n
            m=max(m,k)
            k=1
        n = int(input("Введите число:"))
    m=max(m,k)
    print(m)

n=int(input("Введите число:"))
f(n)

