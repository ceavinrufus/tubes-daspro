from functions.formulas import *
from functions.arraytools import *


def cipher(word, encrypt=True):
    # Mengenkripsi atau mendekripsi dengan metode affine cipher

    # KAMUS LOKAL
    # ciphered : string
    # cipherable : array of character
    # index : integer

    # ALGORITMA
    cipherable = alphanumeric + specialchar
    ciphered = ""

    if encrypt:
        # Menambahkan hasil enkripsi tiap elemen satu per satu
        for i in range(panjang(word)):
            index = lcg(panjang(cipherable), find_index_array(word[i], cipherable))     # Index karakter acak
            ciphered += cipherable[index]
    else: # not encrypt
        # Menambahkan hasil dekripsi tiap elemen satu per satu
        for i in range(panjang(word)):
            index = inverse_lcg(panjang(cipherable), find_index_array(word[i], cipherable))  # Index karakter acak
            ciphered += str(cipherable[index])

    return ciphered
