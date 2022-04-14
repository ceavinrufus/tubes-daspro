user_id = (user id yang sedang login) # ini dari luar, program utamanya nnti. Variabel ini akan dipakai untuk memverifikasi saldo user 

def buy_game ():
  
  IDgame = str(input("Masukkan ID Game: "))
  # asumsi input valid karena tidak ada pada contoh untuk input yang invalid

#-------------------- cek kepemilikan game --------------
  punya = False # asumsikan user belum punya gamenya dulu  
  for i in range(panjang(kepemilikan)): # user_id adalah variabel dummy, harus diganti dan disesuaikan namanya nanti. user_id diasumsikan sebagai variabel yang sedang login saat itu
    if (IDgame == kepemilikan[i][0]) and (user_id == kepemilikan[i][1]):
      punya = True
      print("Anda sudah memiliki Game tersebut!")
      break

#----------------------- cek stok ---------------------------
  if punya == False : 
    stok_game = game[ValidId (IDgame, game)][5]
    harga_game = game[ValidId (IDGame, game)][4]
    saldo = user[user_id][5]
    if (stok_game > 0) :    # pakai variabel dummy

#----------------------- cek saldo --------------------------
      if saldo < harga_game : 
        print("Saldo anda tidak cukup untuk membeli Game tersebut!")
      else : 
        print("Game", "\"" + game[ValidId (IDgame, game)][1] + "\"", "berhasil dibeli!")
        game_belian = [[IDgame, user_id]]
        kepemilikan = kepemilikan + game_belian   # update kepemilikan setelah membeli
        saldo_stlh_beli = saldo - harga_game 
        saldo = saldo_stlh_beli  # update saldo setelah membeli
    else : 
      print("Stok Game tersebut sedang habis!")
