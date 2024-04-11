vars_input = '''
p	g	x	k	M
83	15	30	55	93551
'''

vs = dict(zip(vars_input.strip().split('\n')[0].split(), map(int, vars_input.strip().split('\n')[1].split())))

print(vs)
p = vs['p']
g = vs['g']
x = vs['x']
k = vs['k']
M = vs['M']

hs = [len(str(M))]

for i, el in enumerate(str(M)):
    hs.append(((int(str(M)[i]) + hs[-1]) ** 2) % (p - 1))

hs_M = hs[-1] + 1

print('\n'.join(f"h{i} = {hs[i]}" for i in range(len(hs))))
print(f"h(M) = {hs_M}")

r = g ** k % p

print(f"r = {r}")

rs = [g]
for i in range(k - 1):
    rs.append(rs[-1] * g % p)

print(f"rs = {rs}")

u = (hs_M - x * r) % (p - 1)

print(f"u = {u}")

tmp_c = [p-1, k]
for i in range(0, len(str(M))):
    try:
        tmp_c.append(tmp_c[-2] % tmp_c[-1])
    except: pass

# tmp_d = [1, 0]
# tmp_d = [tmp_d[-2] - tmp_d[-1] * (tmp_c[i] // tmp_c[i + 1]) for i in range(len(str(M)) - 1)]
tmp_f = []
for i in range(len(tmp_c)):
    try:
        tmp_f.append(tmp_c[i] // tmp_c[i + 1])
    except: pass

print(f"tmp_f = {tmp_f}")

tmp_e = [0, 1]
for i in range(0, len(str(M))):
    try:
        tmp_e.append(tmp_e[-2] - tmp_e[-1] * tmp_f[i])
    except: pass

k = next((x for x in reversed(tmp_e) if x > 0), None)

print(f"k = {k}")

s = k * u % (p - 1)

print(f"s = {s}")

y = g ** x % p

print(f"y = {y}")

yr_mod_p = y ** r % p

print(f"yr_mod_p = {yr_mod_p}")

rs_mod_p = r ** s % p
print(f"rs_mod_p = {rs_mod_p}")

yrrs_mod_p = (y ** r * r ** s) % p
print(f"yrrs_mod_p = {yrrs_mod_p}")

gh_mod_p = g ** hs_M % p
print(f"gh_mod_p = {gh_mod_p}")

# 2 вариант
# Экзамен
# Доп вопрос по теме 3.5