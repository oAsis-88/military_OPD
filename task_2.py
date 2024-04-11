a = 21
b = 22
p = 23

x = 2
y = 7

numerator_1 = 3 * x ** 2 + a
denominator_1 = 2 * y

numerator_2 = numerator_1 % p
denominator_2 = denominator_1 % p

print(f"λ = {numerator_1} / {denominator_1} = {numerator_2} / {denominator_2}")

b9 = 1
b10 = 0
c9 = 0
c10 = 1

a9_18 = [p, denominator_2]
for i in range(8):
    try:
        a9_18.append(a9_18[-2] % a9_18[-1])
    except: pass

print(f"a9_18 = {a9_18}")

d11_18 = []
for i in range(8):
    try:
        d11_18.append(a9_18[i] // a9_18[i + 1])
    except:
        pass

print(f"d11_18 = {d11_18}")

b9_18 = [1, 0]
for i in range(6):
    try:
        b9_18.append(b9_18[-2] - b9_18[-1] * d11_18[i])
    except:
        pass

print(f"b9_18 = {b9_18}")

c9_18 = [0, 1]
for i in range(6):
    try:
        c9_18.append(c9_18[-2] - c9_18[-1] * d11_18[i])
    except:
        pass

print(f"c9_18 = {c9_18}")

# b11 = [b9 - b10 * d11[-1]]
# c11 = [c9 - c10 * d11[-1]]
#
# print(b11)
# print(c11)
