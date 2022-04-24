import os
import sys
from procedures.save import save


def exit(header, user, game, riwayat, kepemilikan):
    # I.S. array user, game, riwayat, dan kepemilikan terdefinisi
    # F.S. program berhenti dan data tersimpan ke dalam file jika pengguna ingin menyimpan

    # KAMUS LOKAL
    # ans : string

    # ALGORITMA

    while True:
        ans = input("\nApakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        os.system("cls")
        if ans.upper() == "N" or ans.upper() == "Y":
            if ans.upper() == "Y":
                save(header, user, game, riwayat, kepemilikan)
            sys.exit()
