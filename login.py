from bnmo_function import *
import load

username = input_username("Masukan username: ")
while True:
    password = input("Masukan password: ")
    break

if is_ada(username, load.user):
    for data in load.user:
        if password == data[3]:
            print("Halo {}! Selamat datang di “Binomo”".format(data[2]))
            break
        else:
            print("Password atau username salah atau tidak ditemukan.")
            break
else:
    print("Password atau username salah atau tidak ditemukan.")