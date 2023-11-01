def f(n):
    k=0
    while n!=0:
        n1 = int(input("Введите число:"))
        if n1==n and n1!=0:
            k+=1
        n=n1
    print(k)

n=int(input("Введите число:"))
f(n)

