p = -1
c = 0
m = 0
element = int(input())
while element != 0:
    if p == element:
        c += 1
    else:
        p = element
        m = max(m, c)
        c = 1
    element = int(input())
m= max(m, c)
print(m)
