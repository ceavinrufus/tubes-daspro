def lcg(m, x, a=3, c=5):
    # Fungsi yang mereturn bilangan acak dengan menggunakan metode linear congruential

    # KAMUS LOKAL
    # a, c, x : integer

    # ALGORITMA
    fx = (a*x + c) % m               # Rumus metode linear kongruen

    return fx


def mod_inverse(a, m):
    # Fungsi yang mereturn nilai dari modular multiplicative inverse

    # KAMUS LOKAL

    # ALGORITMA
    for x in range(1, m):
        if a*x % m == 1:
            return x

    return -1


def inverse_lcg(m, fx, a=3, c=5):
    # Fungsi yang mereturn bilangan acak dengan menggunakan metode invers linear congruential generator

    # KAMUS LOKAL
    # a, c, x : integer

    # ALGORITMA
    a_inverse = mod_inverse(a, m)
    x = (a_inverse * (fx - c)) % m

    return x


def absolute(x):
    # Fungsi untuk mengembalikan nilai absolut dari x

    # KAMUS LOKAL

    # ALGORITMA
    if x >= 0:
        return x
    else:
        return -x
