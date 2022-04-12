import sys
from save import *

def exit(user, game, riwayat, kepemilikan):
    # I.S. array user, game, riwayat, dan kepemilikan terdefinisi
    # F.S. program berhenti dan data tersimpan ke dalam file jika pengguna ingin menyimpan

    # KAMUS LOKAL
    # ans : string

    # ALGORITMA
    print("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)", end=" ")

    while True:
        ans = input()
        if ans.upper() != "Y" and ans.upper() != "N":
            print("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)", end=" ")
        else:
            if ans.upper() == "Y":
                save(user, game, riwayat, kepemilikan)
            sys.exit()
