from functions.arraytools import *
from rich import print


def topup(user):
    # I.S. Array user sudah terdefinisi
    # F.S. Saldo ditambah/dikurang sesuai masukan admin

    # KAMUS LOKAL
    # username : string
    # jumlah, saldo, idx : integer

    # ALGORITMA
    username = input("\nMasukan username: ")
    if not uname_valid(username):
        print("[red]Username hanya dapat mengandung alfabet (A-Z, a-z), underscore (_), strip (-), dan angka (0-9)!")
        return

    idx = find_index_matriks(username, user, 1)   # Indeks username yang ditemukan pada array. Jika tidak ditemukan, indeksnya -999

    if idx >= 0:
        jumlah = input("Masukkan saldo: ")
        if not is_numeric(jumlah):
            print("\n[red]Saldo harus berupa angka!")
            return
        else:
            jumlah = int(jumlah)

        saldo = int(user[idx][5]) + jumlah              # Nilai saldo setelah diubah
        if jumlah < 0:
            if saldo >= 0:                              # Jika saldo mencukupi, saldo diubah
                user[idx][5] = saldo
                print("\n[green]Saldo {} berkurang menjadi[/green] {}".format(user[idx][2], saldo))
            else:  # saldo < 0
                print("\n[red]Masukan tidak valid.")
        else: # jumlah >= 0
            user[idx][5] = saldo                       # Mengubah stok pada array
            print("\n[green]Top up berhasil. Saldo {} bertambah menjadi[/green] {}".format(user[idx][2], saldo))
    else:  # idx < 0
        print('\n[red]Username "{}" tidak ditemukan.'.format(username))

    return
