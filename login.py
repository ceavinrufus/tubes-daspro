from unamecheck import *

def login(user):
    # Fungsi yang mereturn atribut user yang login

    # KAMUS LOKAL
    # username, password : string
    # idx : integer
    # isUnameAda : boolean

    # ALGORITMA
    while True:                                         # Menerima input username pengguna
        username = input("Masukan username: ")
        if username_valid(username):                    # Looping berhenti jika username sudah valid
            break
        else:                                           # Jika username masih belum valid, ditampilkan pesan error
            print("Username hanya dapat mengandung alfabet (A-Z, a-z), underscore (_), strip (-), dan angka (0-9)!")
    password = input("Masukan password: ")

    isUnameAda, idx = isuname_ada(username, user)      # Mengecek apakah username ada pada database

    if isUnameAda:
        if user[idx][3] == password:                    # Mengecek apakah password user benar
            print("Halo {}! Selamat datang di “Binomo”".format(user[idx][2]))
            return tuple(user[idx]), True
        else:
            print("Password atau username salah atau tidak ditemukan.")
            return (None, None, None, None, None, None), False
    else:
        print("Password atau username salah atau tidak ditemukan.")
        return (None, None, None, None, None, None), False