import os
from functions.arraytools import *
from rich import print


def is_horizontal(symbol, board):
    # Mengecek apakah bagian horizontal pada board sudah terisi oleh simbol yang sama

    # KAMUS LOKAL
    # horizontal : boolean

    # ALGORITMA
    horizontal = False
    for i in range(panjang(board)):
        horizontal = True
        for j in range(panjang(board)):
            if symbol != board[i][j]:   # Mengecek apakah dalam satu baris simbolnya sama semua
                horizontal = False
        if horizontal:
            break

    return horizontal


def is_vertikal(symbol, board):
    # Mengecek apakah bagian vertikal pada board sudah terisi oleh simbol yang sama

    # KAMUS LOKAL
    # vertikal : boolean

    # ALGORITMA
    vertikal = False
    for j in range(panjang(board)):
        vertikal = True
        for i in range(panjang(board)):
            if symbol != board[i][j]:   # Mengecek apakah dalam satu kolom simbolnya sama semua
                vertikal = False
        if vertikal:
            break

    return vertikal


def is_diagonal(symbol, board):
    # Mengecek apakah bagian diagonal pada board sudah terisi oleh simbol yang sama

    # KAMUS LOKAL
    # diagonal : boolean

    # ALGORITMA
    diagonal = True
    for i in range(panjang(board)):
        if symbol != board[i][i]:   # Mengecek apakah diagonal ke kanan bawah simbolnya sama semua
            diagonal = False

    if not diagonal:
        diagonal = True
        for i in range(panjang(board)):
            if symbol != board[i][panjang(board) - i - 1]:     # Mengecek apakah diagonal ke kiri bawah simbolnya sama semua
                diagonal = False

    return diagonal


def is_kosong(empty, board):
    # Mengecek apakah masih ada bagian board yang belum terisi

    # KAMUS LOKAL
    # kosong : boolean

    # ALGORITMA
    kosong = False
    for i in range(panjang(board)):
        for j in range(panjang(board)):
            if board[i][j] == empty:    # Mengecek apakah suatu kotak kosong
                kosong = True

    return kosong


def simbol(giliran):
    # Fungsi yang mereturn simbol yang digunakan pemain berdasarkan urutan giliran

    # KAMUS LOKAL

    # ALGORITMA
    if giliran % 2 == 1:
        return 'X'
    else:  # giliran % 2 == 0
        return 'O'


def cetakpapan(board):
    # I.S. Matriks board terdefinisi
    # F.S. Mencetak board tic tac toe

    # KAMUS LOKAL

    # ALGORITMA
    os.system("cls")            # Mengosongkan tampilan pada terminal
    print("\nStatus Papan")
    for i in range(panjang(board)):
        print(joining(board[i], delimiter=""))  # Mencetak board baris per baris


def is_win(smbl, board):
    # Fungsi yang mereturn True jika pada board ada yang memenuhi kriteria untuk menang, False jika sebaliknya

    # KAMUS LOKAL
    # win : boolean

    # ALGORITMA
    win = False
    if is_vertikal(smbl, board):
        print("\n[cyan]{} menang secara vertikal.".format(smbl))
        win = True
    elif is_horizontal(smbl, board):
        print("\n[cyan]{} menang secara horizontal.".format(smbl))
        win = True
    elif is_diagonal(smbl, board):
        print("\n[cyan]{} menang secara diagonal.".format(smbl))
        win = True
    return win