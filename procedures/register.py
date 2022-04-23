import os
from functions.arraytools import *
from functions.cipher import cipher
from rich import print


def register(user):
    # I.S. Array user terdefinisi
    # F.S. Ditambahkan data berupa array ke dalam array user

    # KAMUS LOKAL
    # nama, username, password : string
    # idx : integer
    # allowed_uname, allowed_password : array of character

    # ALGORITMA
    allowed_uname = alphanumeric + ['_', '-']
    allowed_password = alphanumeric + specialchar

    nama = input("\nMasukkan nama: ")
    os.system("cls")
    while True:
        print("\nMasukkan nama:", nama)
        username = stripping(input("Masukkan username: "))
        os.system("cls")
        if panjang(username) == 0:
            print("[red]Username tidak boleh kosong!")
        else:
            if is_subset(username, allowed_uname):                # Looping berhenti jika username sudah valid
                break
            else:                                       # Jika username masih belum valid, ditampilkan pesan error
                print("[red]Username hanya dapat mengandung alfabet (A-Z, a-z), underscore (_), strip (-), dan angka (0-9)!")

    while True:
        print("\nMasukkan nama:", nama)
        print("Masukkan username:", username)
        password = stripping(input("Masukkan password: "))
        os.system("cls")
        if panjang(password) == 0:
            print("[red]Password tidak boleh kosong!")
        else:
            if is_subset(password, allowed_password):                # Looping berhenti jika password sudah valid
                break
            else:                                       # Jika username masih belum valid, ditampilkan pesan error
                print("[red]Password mengandung karakter yang tidak valid")

    idx = find_index_matriks(username, user, 1)       # Indeks username yang ditemukan pada array. Jika tidak ditemukan, indeksnya -999

    if idx >= 0:
        print("Username [red]{}[/red] sudah terpakai, silakan menggunakan username lain.".format(username))
    else: # Jika username tidak ada pada database, akun berhasil dibuat
        user += [[panjang(user) + 1, username, nama, cipher(password), "user", 0]]
        print('Username [red]{}[/red] telah berhasil register ke dalam "Binomo".'.format(username))

    return
