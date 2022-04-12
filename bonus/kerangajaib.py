from functions.formulas import lcg
from functions.arraytools import panjang

input("Apa pertanyaanmu? ")

replies = ["hah", "gatau", "iyah", "hmm", 'g']

print()
print(replies[lcg(panjang(replies))])
