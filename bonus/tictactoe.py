from functions.gametools import *


def tictactoe():
    # Program yang mensimulasikan game tictactoe. Terdapat 2 pemain, yaitu pemain “X” dan pemain “O” yang secara
    # bergiliran bertukar melakukan input yang valid

    # KAMUS LOKAL
    # board : array of array of character
    # giliran, kolom, baris : integer
    # valid, win : boolean
    # smbl : character

    # ALGORITMA
    board = [['#', '#', '#'],
             ['#', '#', '#'],
             ['#', '#', '#']]

    print("Legenda:")
    print("X Pemain 1")
    print("O Pemain 2")

    print("\nStatus Papan")
    for i in range(panjang(board)):
        print(joining(board[i], delimiter=""), end="\n")        # Mencetak board baris per baris

    giliran = 0
    win = False
    while not win and is_kosong(board):  # Loop berhenti jika ada yang menang atau board sudah tidak bisa diisi lagi
        giliran += 1
        smbl = simbol(giliran)

        valid = False
        while not valid:    # Loop akan berhenti jika input pemain sudah valid
            print('\nGiliran pemain "{}"'.format(smbl))
            try:
                kolom = int(input("Kolom: ")) - 1
                baris = int(input("Baris: ")) - 1

                if baris >= panjang(board) or kolom >= panjang(board):  # Mengecek apakah input sesuai dengan indeks array (board)
                    print("\nKotak tidak valid")
                else:
                    if board[baris][kolom] != '#':      # Mengecek apakah kotak yang ingin diisi sudah terisi atau belum
                        print("\nKotak sudah terisi. Silakan pilih kotak lain.")
                    else:
                        board[baris][kolom] = smbl
                        print("\nStatus Papan")
                        for i in range(panjang(board)):
                            print(joining(board[i], delimiter=""), end="\n")        # Mencetak board baris per baris
                        valid = True
            except ValueError:          # Jika input baris atau kolom bukan bilangan bulat
                print("Input harus berupa bilangan bulat!")

        # Mengecek apakah sudah ada yang menang (Secara vertikal atau horizontal atau diagonal)
        if is_vertikal(smbl, board):
            print("\n{} menang secara vertikal.".format(smbl))
            win = True
        elif is_horizontal(smbl, board):
            print("\n{} menang secara horizontal.".format(smbl))
            win = True
        elif is_diagonal(smbl, board):
            print("\n{} menang secara diagonal.".format(smbl))
            win = True

    if not win:     # Jika loop berhenti tetapi belum ada yang menang
        print("Seri. Tidak ada yang menang.")
