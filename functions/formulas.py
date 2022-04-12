import time

def lcg(m, x=1, a=5):
    # Fungsi yang mereturn bilangan acak dengan menggunakan metode linear congruential generator

    # KAMUS LOKAL
    # a, c, x : integer

    # ALGORITMA
    c = time.gmtime().tm_sec        # Nilai c merupakan nilai detik

    x = (a*x + c) % m               # Rumus linear congruentiaal generator

    return x


def absolute(x):
    # Fungsi untuk mengembalikan nilai absolut dari x

    # KAMUS LOKAL

    # ALGORITMA
    if x >= 0:
        return x
    else:
        return -x
