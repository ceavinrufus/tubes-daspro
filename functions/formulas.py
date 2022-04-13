def linear_congruential(m, x, a=5, c=3):
    # Fungsi yang mereturn bilangan acak dengan menggunakan metode linear congruential

    # KAMUS LOKAL
    # a, c, x : integer

    # ALGORITMA
    fx = (a*x + c) % m               # Rumus metode linear kongruen

    return fx


def modInverse(a, m):
    # Fungsi yang mereturn nilai dari modular multiplicative inverse
    for x in range(1, m):
        if a*x % m == 1:
            return x
    return -1


def inverse_linear_congruential(m, fx, a=5, c=3):
    # Fungsi yang mereturn bilangan acak dengan menggunakan metode invers linear congruential generator

    # KAMUS LOKAL
    # a, c, x : integer

    # ALGORITMA
    a_inverse = modInverse(a, m)
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
