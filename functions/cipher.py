from functions.formulas import lcg, inv_lcg
from functions.arraytools import *

allowed = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
           '_', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ',
           '@', '%', '+', '/', '!', '#', '$', '?', ':', '.', '(', ')', '~',
           '^', '&', '*', '=', '{', '[', '}', ']', '|', '<', '>']


def encrypt(string):
    # Mengenkripsi string dengan affine cipher

    # KAMUS LOKAL
    # encrypted : string

    # ALGORITMA
    encrypted = str(lcg(panjang(allowed), findIndex(string[0], allowed)))       # Inisialisasi variabel

    # Menambahkan hasil enkripsi tiap elemen satu per satu
    for i in range(1, panjang(string)):
        encrypted += ","
        encrypted += str(lcg(panjang(allowed), findIndex(string[i], allowed)))

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
        index = inv_lcg(panjang(allowed), int(i))
        decrypted += allowed[index]

    return decrypted
