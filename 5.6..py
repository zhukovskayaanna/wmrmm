def f(n):
    k=0
    sum=0
    while n!=0:
        k+=1
        sum+=n
        n=int(input("Введите число:"))
    print(sum/k)

n=int(input("Введите число:"))
f(n)

