from functions.formulas import *
from functions.arraytools import *


def encrypt(word):
    # Mengenkripsi string dengan metode affine cipher

    # KAMUS LOKAL
    # encrypted : string
    # cipherable : array of character
    # index : integer

    # ALGORITMA
    cipherable = alphanumeric + specialchar

    encrypted = ""

    # Menambahkan hasil enkripsi tiap elemen satu per satu
    for i in range(panjang(word)):
        index = lcg(panjang(cipherable), find_index_array(word[i], cipherable))     # Index karakter acak
        encrypted += cipherable[index]

    return encrypted


def decrypt(word):
    # Mendekripsi string dengan metode affine cipher

    # KAMUS LOKAL
    # decrypted : string
    # cipherable : array of character
    # index : integer

    # ALGORITMA
    cipherable = alphanumeric + specialchar

    decrypted = ""

    # Menambahkan hasil dekripsi tiap elemen satu per satu
    for i in range(panjang(word)):
        index = inverse_lcg(panjang(cipherable), find_index_array(word[i], cipherable))     # Index karakter acak
        decrypted += str(cipherable[index])

    return decrypted
