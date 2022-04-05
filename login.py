from bnmo_function import *
import load

while True:                                         # Menerima input username pengguna
    username = input("Masukan username: ")
    if username_valid(username):                    # Looping berhenti jika username sudah valid
        break
    else:                                           # Jika username masih belum valid, ditampilkan pesan error
        print("Username hanya dapat mengandung alfabet (A-Z, a-z), underscore (_), strip (-), dan angka (0-9)!")
password = input("Masukan password: ")

isUnameAda, idx = isuname_ada(username, load.user)      # Menampung keluaran dari fungsi is_ada

if isUnameAda:
    if load.user[idx][3] == password:
        print("Halo {}! Selamat datang di “Binomo”".format(load.user[idx][2]))
    else:
        print("Password atau username salah atau tidak ditemukan.")
else:
    print("Password atau username salah atau tidak ditemukan.")
