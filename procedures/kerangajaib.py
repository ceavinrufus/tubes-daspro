import os
import time
from rich import print
from functions.formulas import lcg
from functions.arraytools import panjang


def kerangajaib():
    # Mensimulasikan magic conch shell
    # I.S. Array replies terdefinisi
    # F.S. Ditampilkan jawaban yang diambil dari array replies secara pseudorandom

    # KAMUS LOKAL
    # replies : array of string

    # ALGORITMA
    os.system("cls")
    replies = ["hah", "gatau", "iyah", "hmm", "g"]  # List jawaban yang bisa dikeluarkan

    input("Apa pertanyaanmu? ")

    second = time.gmtime().tm_sec
    print("\n[green]{}".format(replies[lcg(panjang(replies), second)]))
