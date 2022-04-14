from functions.tictactools import *


def tictactoe():
    # Mensimulasikan game tictactoe. Terdapat 2 pemain, yaitu pemain “X” dan pemain “O” secara bergiliran
    # I.S. Matriks board terdefinisi
    # F.S. Game tictactoe berakhir dengan salah satu pemain sebagai pemenang atau keduanya seri

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

    cetakpapan(board)

    giliran = 0
    win = False
    while not win or is_kosong(board, '#'):  # Loop berhenti jika ada yang menang atau board sudah tidak bisa diisi
        giliran += 1
        smbl = simbol(giliran)

        valid = False
        while not valid:    # Loop akan berhenti jika input pemain sudah valid
            print('\nGiliran pemain "{}"'.format(smbl))
            try:
                kolom = int(input("Kolom: ")) - 1
                baris = int(input("Baris: ")) - 1
            except ValueError:  # Jika input baris atau kolom bukan bilangan bulat
                cetakpapan(board)
                print("\n[red]Input harus berupa bilangan bulat.")
                continue

            if baris >= panjang(board) or kolom >= panjang(board):  # Mengecek apakah input sesuai dengan indeks array (board)
                cetakpapan(board)
                print("\n[red]Kotak tidak valid.")
            else:
                if board[baris][kolom] != '#':      # Mengecek apakah kotak yang ingin diisi sudah terisi atau belum
                    cetakpapan(board)
                    print("\n[red]Kotak sudah terisi. Silakan pilih kotak lain.")
                else:
                    board[baris][kolom] = smbl
                    cetakpapan(board)
                    valid = True


        # Mengecek apakah sudah ada yang menang (Secara vertikal atau horizontal atau diagonal)
        win = is_win(smbl, board)

    if not win:     # Jika loop berhenti tetapi belum ada yang menang
        print("Seri. Tidak ada yang menang.")

    return
