from functions.unamecheck import *
from rich import print
from functions.cipher import encrypt


def register(user):
    # KAMUS LOKAL
    # nama, username, password, uname : string
    # idx : integer

    # ALGORITMA
    nama = input("Masukan nama: ")                  # Menerima input nama pengguna
    while True:                                     # Menerima input username pengguna
        username = input("Masukan username: ")
        if username_valid(username):                # Looping berhenti jika username sudah valid
            break
        else: # Jika username masih belum valid, ditampilkan pesan error
            print("Username hanya dapat mengandung alfabet (A-Z, a-z), underscore (_), strip (-), dan angka (0-9)!")
    password = input("Masukan password: ")          # Menerima input password pengguna

    idx = isuname_ada(username, user)       # Indeks username yang ditemukan pada array. Jika tidak ditemukan, indeksnya -999

    if idx >= 0:
        print("Username [red]{}[/red] sudah terpakai, silakan menggunakan username lain.".format(username))
    else: # Jika username tidak ada pada database, akun berhasil dibuat
        print('Username [red]{}[/red] telah berhasil register ke dalam "Binomo".'.format(username))
        user += [[panjang(user)+1, username, nama, encrypt(password), "user", 0]]