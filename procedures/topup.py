def topup ():
    
  nama = str(input("Masukkan username: "))
  ubahsaldo = int(input("Masukkan saldo: ")

  idx = isuname_ada (nama, user)
  if idx == -999 :
    print("Username", "\"" + nama + "\"", "tidak ditemukan.")
  else : 
    saldo_baru = user[idx][5] + ubahsaldo
    if saldo_baru < 0 :
      print("Masukan tidak valid.")
    elif saldo_baru >= 0 :  
      print("Top up berhasil. Saldo", nama, "bertambah menjadi", saldo_baru + ".")
