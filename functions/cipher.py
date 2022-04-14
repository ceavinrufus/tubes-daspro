from functions.formulas import *
from functions.arraytools import *

cipherable = alphanumeric + specialchar

def encrypt(string):
    # Mengenkripsi string dengan affine cipher

    # KAMUS LOKAL
    # encrypted : string

    # ALGORITMA
    encrypted = str(linear_congruential(panjang(cipherable), find_index_array(string[0], cipherable)))       # Inisialisasi variabel

    # Menambahkan hasil enkripsi tiap elemen satu per satu
    for i in range(1, panjang(string)):
        encrypted += ","
        encrypted += str(linear_congruential(panjang(cipherable), find_index_array(string[i], cipherable)))

    return encrypted


def decrypt(string):
    # Mendekripsi string dengan affine cipher

    # KAMUS LOKAL
    # decrypted : string

    # ALGORITMA
    arr = splitting(string, delimiter=",")      # Memisahkan delimiter dari string
    decrypted = ""                              # Inisiasi variabel

    # Menambahkan hasil dekripsi tiap elemen satu per satu
    for i in arr:
        index = inverse_linear_congruential(panjang(cipherable), int(i))
        decrypted += cipherable[index]

    return decrypted
