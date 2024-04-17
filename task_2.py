def task_2(P=None, Q=None, R=None, k=None):
    a = a2 = 21
    b = b2 = 22
    p = c2 = 23

    x_R = 2
    y_R = 7
    print(f"P = {P}")

    numerator_1 = 3 * x_R ** 2 + a2
    denominator_1 = 2 * y_R

    print_rows_6_7 = f"λ = {numerator_1} / {denominator_1}"
    print(print_rows_6_7)

    numerator_2 = numerator_1 % c2
    denominator_2 = denominator_1 % c2

    print_rows_6_7 += f" = {numerator_2} / {denominator_2}"
    print(print_rows_6_7)

    a9_18 = [c2, denominator_2]
    d11_18 = []
    for i in range(8):
        try:
            a9_18.append(a9_18[-2] % a9_18[-1])
            d11_18.append(a9_18[i] // a9_18[i + 1])
        except:
            pass

    print(f"a9_18 = {a9_18}")
    print(f"d11_18 = {d11_18}")

    b9_18 = [1, 0]
    c9_18 = [0, 1]

    for i in range(6):
        try:
            b9_18.append(b9_18[-2] - b9_18[-1] * d11_18[i])
            c9_18.append(c9_18[-2] - c9_18[-1] * d11_18[i])
        except:
            pass

    print(f"b9_18 = {b9_18}")
    print(f"c9_18 = {c9_18}")

    index = a9_18[::-1].index(1)

    result_3 = numerator_2 * c9_18[-index - 1]

    print_rows_6_7 += f" = {result_3}"
    print(print_rows_6_7)

    alpha = result_4 = result_3 % c2

    print_rows_6_7 += f" = {result_4}"
    print(print_rows_6_7)

    a20 = '2p'
    b20 = 'x_R ='
    b21 = 'y_R ='

    print(a20)

    x_2p = c20 = (alpha ** 2 - 2 * x_R) % c2

    print(f"{b20} {c20}")

    y_2p = c21 = (-y_R + alpha * (x_R - x_2p)) % c2

    print(f"{b21} {c21}")

    a23 = "Проверка"
    b23 = "левая часть"
    b24 = "правая часть"

    print(a23)

    c23 = y_2p ** 2 % c2
    c24 = (x_2p ** 3 + a2 * x_2p + b2) % c2

    print(f"{b23} {c23}")
    print(f"{b24} {c24}")

    j1 = "Q"
    j3 = "R"

    j2, k2 = Q
    j4, k4 = R

    print(j1)
    print(Q)
    print(j3)
    print(R)

    j6 = "λ ="
    k6 = (k4 - k2) % c2
    k7 = (j4 - j2) % c2

    print(f"{j6} {k6} / {k7}")

    j9_18 = [c2, k7]
    m11_18 = []
    for i in range(8):
        try:
            j9_18.append(j9_18[-2] % j9_18[-1])
            m11_18.append(j9_18[i] // j9_18[i + 1])
        except:
            pass

    print(f"j9_18 = {j9_18}")
    print(f"m11_18 = {m11_18}")

    k9_18 = [1, 0]
    l9_18 = [0, 1]

    for i in range(6):
        try:
            k9_18.append(k9_18[-2] - k9_18[-1] * m11_18[i])
            l9_18.append(l9_18[-2] - l9_18[-1] * m11_18[i])
        except:
            pass

    print(f"k9_18 = {k9_18}")
    print(f"l9_18 = {l9_18}")

    index = j9_18[::-1].index(1)
    m6 = k6 * l9_18[-index - 1] % c2

    print(f"{j6} {k6} / {k7} = {m6}")

    j20 = "Q + R"
    k20 = "x_R ="
    k21 = "y_R ="

    print(j20)

    l20 = x_q_r = (m6 ** 2 - j2 - j4) % c2

    print(f"{k20} {l20}")

    l21 = y_q_r = (-k2 + m6 * (j2 - l20)) % c2

    print(f"{k21} {l21}")

    j23 = "Проверка"
    k23 = "левая часть"
    k24 = "правая часть"

    print(j23)

    l23 = y_q_r ** 2 % c2
    l24 = (x_q_r ** 3 + a2 * x_q_r + b2) % c2

    print(f"{k23} {l23}")
    print(f"{k24} {l24}")

    print("======================================  Задание 2  ======================================")
    S1 = 2 * P
    S2 = 2 * P + P
    S3 = 2 * Q
    S4 = S2 + S3
    S5 = -R  # = x_R - y_R
    S = S4 + S5
    print(f"S1 = {S1}")
    print(f"S2 = {S2}")
    print(f"S3 = {S3}")
    print(f"S4 = {S4}")
    print(f"S5 = {S5}")
    print(f"S = {S}")


if __name__ == "__main__":
    Q = (2, 7)
    R = (12, 22)

    task_2(
        P=(8, 9),
        Q=(7, 12),
        R=(21, 15),
        k=12
    )
