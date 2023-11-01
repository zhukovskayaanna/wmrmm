x = 2
y = 3
radius = 5

f = (6, 12)
l = (-5, 5)
p = (-2, 2)

def ne_okr(x, y, a, b, r):
    b1 = (x - a)**2 + (y - b)**2
    return b1 <= r**2

def v(p, f, l, a, b, r):
    count = 0

    if ne_okr(p[0], p[1], a, b, r):
        count += 1

    if ne_okr(f[0], f[1], a, b, r):
        count += 1

    if ne_okr(l[0], l[1], a, b, r):
        count += 1

    return count

result = v(p, f, l, x, y, radius)
print('Количество точек внутри окружности:', result)

