from bnmo_function import *
from ParsingConverting import *
def validcode (code):
    for i in range (panjang(game)):
        masukan = False
        if code == game[i][5]:
            masukan = True
            break
        else :
            masukan = False
    return masukan

def indexganti(code):
    counter = -1
    for i in range (panjang(game)):
        counter += 1
        found = False
        if code == game[i][5]:
            found == True
            break
    return counter

def ubah_game(game):    
    while True:
        code = input("Masukkan game code : ")
        if not validcode(code):
            print("Code Game tidak valid. Silakan masukkan code game kembali")
        else:
            nama_game = input("Masukkan nama game : ")
            kategori = input("Masukkan kategori : ")
            tahun_rilis = input("Masukkan tahun rilis : ")
            harga = input("Masukkan harga : ")
            stok_awal = input("Masukkan stok awal : ")
            if nama_game == '':
                game[indexganti(code)][0] = game[indexganti(code)][0]
            else:
                game[indexganti(code)][0] = nama_game
            if kategori == '':
                game[indexganti(code)][1] = game[indexganti(code)][1]
            else:
                game[indexganti(code)][1] = kategori
            if tahun_rilis == '':
                game[indexganti(code)][2] = game[indexganti(code)][2]
            else:
                game[indexganti(code)][2] = tahun_rilis
            if harga == '' :
                game[indexganti(code)][3] = game[indexganti(code)][3]
            else:
                game[indexganti(code)][3] = harga
            if stok_awal == '' :
                game[indexganti(code)][4] = game[indexganti(code)][4]
            else:
                game[indexganti(code)][4] = stok_awal
        return game

        

