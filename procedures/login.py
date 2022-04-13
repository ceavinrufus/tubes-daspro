from functions.unamecheck import *
from rich import print
from functions.cipher import decrypt

def login(user):
    # Fungsi yang meminta username dan password kemudian mereturn indeks user jika berhasil login dan mereturn
    # -999 jika gagal login

    # KAMUS LOKAL
    # username, password : string
    # idx : integer
    # isUnameAda : boolean

    # ALGORITMA
    while True:                                         # Menerima input username pengguna
        username = input("\nMasukan username: ")
        if username_valid(username):                    # Looping berhenti jika username sudah valid
            break
        else:                                           # Jika username masih belum valid, ditampilkan pesan error
            print("Username hanya dapat mengandung alfabet (A-Z, a-z), underscore (_), strip (-), dan angka (0-9)!")
    password = input("Masukan password: ")

    idx = isuname_ada(username, user)      # Indeks username yang ditemukan pada array. Jika tidak ditemukan, indeksnya -999

    if idx >= 0 and decrypt(user[idx][3]) == password:                    # Mengecek apakah password user benar
        return idx
    else:
        print("Password atau username salah atau tidak ditemukan.")
        return -999