import time
from functions.arraytools import panjang

def lcg(x, m):
    # Fungsi yang mereturn bilangan acak dengan menggunakan metode linear congruential generator

    # KAMUS LOKAL
    # a, c, x : integer

    # ALGORITMA
    a = 5
    c = time.gmtime().tm_sec        # Nilai c merupakan nilai detik

    x = (a*x + c) % m               # Rumus linear congruentiaal generator

    return x

if input() == "kerangajaib":
    input("Apa pertanyaanmu? ")

    replies = ["hah", "gatau", "iyah", "hmm", 'g']

    print()
    print(replies[lcg(0, panjang(replies))])