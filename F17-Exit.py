from bnmo_function import *
from save import *
print("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
while True:
    ans = input()
    if ans.upper() != "Y" and ans.upper() != "N":
        print("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
    else:
        if ans.upper() == "Y":
            save_file
            print("Saving data")
        else :
            print("minta perintah lagi")
        break
        