import os
import sys
from procedures.save import save


def exit(header, user, game, riwayat, kepemilikan):
    # I.S. array user, game, riwayat, dan kepemilikan terdefinisi
    # F.S. program berhenti dan data tersimpan ke dalam file jika pengguna ingin menyimpan

    # KAMUS LOKAL
    # ans : string

    # ALGORITMA
    print("\nApakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)", end=" ")

    while True:
        ans = input()
        if ans.upper() != "Y" and ans.upper() != "N":
            os.system("cls")
            print("\nApakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)", end=" ")
        else:
            if ans.upper() == "Y":
                save(header, user, game, riwayat, kepemilikan)
            os.system("cls")
            sys.exit()
