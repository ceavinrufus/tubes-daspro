from functions.arraytools import *
from functions.cipher import decrypt
from rich import print


def login(user):
    # Fungsi yang meminta username dan password kemudian mereturn indeks user jika berhasil login dan mereturn
    # -999 jika gagal login

    # KAMUS LOKAL
    # username, password : string
    # idx : integer

    # ALGORITMA
    username = input("\nMasukan username: ")
    password = input("Masukan password: ")

    idx = find_index_matriks(username, user, 1)      # Indeks username yang ditemukan pada array. Jika tidak ditemukan, indeksnya -999

    if idx >= 0 and decrypt(user[idx][3]) == password:                    # Mengecek apakah password user benar
        return idx
    else:
        print("Password atau username salah atau tidak ditemukan.")
        return -999
