from functions.arraytools import find_index_matriks
from rich import print


def topup(user):
    # I.S. Array user sudah terdefinisi
    # F.S. Saldo ditambah/dikurang sesuai masukan admin

    # KAMUS LOKAL
    # username : string
    # jumlah, saldo : integer

    # ALGORITMA
    username = input("\nMasukan username: ")
    try:
        jumlah = int(input("Masukkan saldo: "))
    except ValueError:
        print("[red]Saldo harus berupa angka!")
        return

    idx = find_index_matriks(username, user, 1)   # Indeks username yang ditemukan pada array. Jika tidak ditemukan, indeksnya -999

    if idx >= 0:
        saldo = int(user[idx][5]) + jumlah              # Nilai saldo setelah diubah
        if jumlah < 0:
            if saldo >= 0:                              # Jika saldo mencukupi, saldo diubah
                user[idx][5] = jumlah
                print("Top up berhasil. Saldo", user[idx][2], "berkurang menjadi", saldo)
            else:  # saldo < 0
                print("Masukan tidak valid.")
        else: # jumlah >= 0
            user[idx][5] = jumlah                       # Mengubah stok pada array
            print("Top up berhasil. Saldo", user[idx][2], "bertambah menjadi", saldo)
    else:  # idx < 0
        print('Username "{}" tidak ditemukan.'.format(username))

    return