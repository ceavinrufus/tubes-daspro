import load
from bnmo_function import *

# KAMUS
# nama, username, password, uname : string
# uname_ada : boolean

# ALGORITMA
nama = input("Masukan nama: ")                  # Menerima input nama pengguna
while True:                                     # Menerima input username pengguna
    username = input("Masukan username: ")
    if username_valid(username):                # Looping berhenti jika username sudah valid
        break
    else: # Jika username masih belum valid, ditampilkan pesan error
        print("Username hanya dapat mengandung alfabet (A-Z, a-z), underscore (_), strip (-), dan angka (0-9)!")
password = input("Masukan password: ")          # Menerima input password pengguna

isUnameAda, idx = isuname_ada(username, load.user)  # Menampung keluaran dari fungsi is_ada

if isUnameAda:
    print("Username", load.user[idx][1], "sudah terpakai, silakan menggunakan username lain.")
else: # Jika username tidak ada pada database, akun berhasil dibuat
    print("Username", username, "telah berhasil register ke dalam ”Binomo”.")
    load.user += [[panjang(load.user)+1, username, nama, password, "user", 0]]