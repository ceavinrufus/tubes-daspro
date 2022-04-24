from functions.arraytools import *
from functions.cipher import cipher
from rich import print


def login(user):
    # Fungsi yang meminta username dan password kemudian mereturn indeks user jika berhasil login dan mereturn
    # -999 jika gagal login

    # KAMUS LOKAL
    # username, password : string
    # idx : integer

    # ALGORITMA
    username = stripping(input("\nMasukan username: "))
    if not uname_valid(username):
        print("[red]Username hanya dapat mengandung alfabet (A-Z, a-z), underscore (_), strip (-), dan angka (0-9)!")
        return -999, False

    password = stripping(input("Masukan password: "))

    idx = find_index_matriks(username, user, 1)      # Indeks username yang ditemukan pada array. Jika tidak ditemukan, indeksnya -999

    if idx >= 0 and cipher(user[idx][3], encrypt=False) == password:                    # Mengecek apakah password user benar
        return idx, True
    else:
        print("[red]Password atau username salah atau tidak ditemukan.")
        return -999, False
