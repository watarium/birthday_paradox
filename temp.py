n = 1
p = 1
while True:
    p = (65534 - n) / 65535
    n += 1
    p *= p
    pp = 1 - p
    if pp >= 0.5:
        print(n)
        print(pp)
        break
