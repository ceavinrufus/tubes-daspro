from functions.arraytools import *

allowed = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
           '_', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def username_valid(username):
    # Fungsi yang menerima masukan username dan mengembalikan nilai apakah username hanya berisi
    # elemen pada list allowed

    # KAMUS LOKAL
    # count : integer

    # ALGORITMA
    count = 0

    # Mengecek apakah setiap karakter pada username valid (terdapat pada list allowed)
    for i in range(panjang(username)):
        if username[i] in allowed:
            count += 1

    return count == panjang(username)

def isuname_ada(username, datasource):
    # Fungsi yang mereturn indeks user jika ditemukan pada array. Jika tidak ditemukan, maka fungsi mereturn -999
    # Username diasumsikan tidak case sensitive.

    # KAMUS LOKAL
    # ada : boolean
    # idx : integer

    # ALGORITMA
    idx = 0
    ada = datasource[idx][1].upper() == username.upper()

    # Mengecek apakah username ada pada array of array of user data
    while idx < panjang(datasource)-1 and not ada:
        idx += 1
        ada = datasource[idx][1].upper() == username.upper()

    if not ada:
        idx = -999

    return idx