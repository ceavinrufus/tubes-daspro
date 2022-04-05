import load
from bnmo_function import *

nama = input("Masukan nama: ")
username = input_username("Masukan username: ")
password = input("Masukan password: ")

uname_ada, uname = is_ada(username, load.user)
if uname_ada:
    print("Username", uname, "sudah terpakai, silakan menggunakan username lain.")
else:
    print("Username", username, "telah berhasil register ke dalam ”Binomo”.")
    load.user += [[panjang(load.user)+1, username, nama, password, "user", 0]]