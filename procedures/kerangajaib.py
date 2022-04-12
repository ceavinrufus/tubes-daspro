from functions.formulas import lcg
from functions.arraytools import panjang


def kerangajaib(replies):
    # Mensimulasikan magic conch shell
    # I.S. Array replies terdefinisi
    # F.S. Ditampilkan jawaban yang diambil dari array replies secara pseudorandom

    # KAMUS LOKAL

    # ALGORITMA
    input("Apa pertanyaanmu? ")

    print()
    print(replies[lcg(panjang(replies))])
