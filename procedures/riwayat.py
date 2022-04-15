
def riwayat ():
    if riwayat == [[]] :  # ini array dari file riwayat csv nya yak aslinya kalau mau diganti ya gpp
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.")
    else : 
        for i in range (1, panjang(riwayat)) :
            print(str(i), end = ". ") 
            print("{:7.6}|".format(riwayat[i][0]), end=" ")
            print("{:21.20}|".format(riwayat[i][1]), end=" ")
            print("{:7.6}|".format(riwayat[i][2]), end=" ")
            print("{:5.4}|".format(riwayat[i][4]), end=" ")
