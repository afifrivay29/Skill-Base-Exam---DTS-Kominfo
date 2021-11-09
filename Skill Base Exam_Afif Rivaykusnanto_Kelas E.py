#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Soal No.1

rupiah = int(input("Masukkan Uang Anda: "))

dolar = rupiah / 14591

print("Rp. ", rupiah, "==> US$", dolar)


# In[2]:


# Soal No.2

beratBadan = float(input("Berat Badan Anda: "))
tinggiBadan = float(input("Tinggi Badan Anda: "))

bmi = beratBadan / (tinggiBadan/100)**2

if 18.5 < bmi < 22.9:
    print("Berat Badan Ideal", bmi)
elif bmi > 22.9:
    print("Berat Badan Overweight", bmi)
elif bmi < 18.5:
    print("Berat Badan Underweight", bmi)


# In[5]:


# Soal No.3

sheila = []

sheila.append("eros")
sheila.append("duta")

for i in range (3):
    nama = input("Masukan Nama Anda: ")
    sheila.append(nama)

try:
    sheila.remove("sakti")
    sheila.remove("anton")
except:
    print("sakti dan anton tidak ada di dalam list")

sheila.insert(len(sheila),"brian")

i = 0
while i < len(sheila):
    print (sheila[i])
    i += 1


# In[6]:


# Soal No.4

hapusVokal = input("Masukan Kata/Kalimat: ")
vokal = ["A", "I", "U", "E", "O"]

for letter in hapusVokal:
    if letter.upper() in vokal:
        continue
    print(letter.upper(), end='')


# In[10]:


# Soal No.5

peserta = {
    "Nama": "Afif Rivaykusnanto",
    "Umur":  21,
    "Keterangan": "Peserta Coding Teacher Academy"
}

for key in peserta:
    print(key, "==>", peserta[key])

peserta["nilaiKuis"] = [85, 78, 60, 90, 88]

sum = 0

for nilaiKuis in peserta["nilaiKuis"]:
    sum += nilaiKuis
    
print("Nilai Kuis Anda: ", sum/len(peserta["nilaiKuis"]))


# In[11]:


# Soal No.6

class Rekening:
    def __init__(self):
        self.__saldo = 500
        self.__limit = 1000
    
    def debit(self, jumlah):
        if self.__limit < jumlah:
            print("Gagal Debit, Jumlah melebihi limit")
        elif self.__saldo < jumlah:
            print(("Gagal Debit, jumlah melebihi saldo"))
            return
        
        if jumlah < 0:
            print("Gagal Debit, Jumlah tidak bisa kurang dari 0")
            return
        
        self.__saldo -= jumlah
        
    def kredit(self, jumlah):
        if jumlah > (4*self.__limit):
            print("Gagal kredit, Jumlah tidak boleh melebihi dari 4 kali limit")
            return
        
        self.__saldo += jumlah
        
    def cetakSaldo(self):
        print("saldo saat ini: " + str(self.__saldo))

briAfif = Rekening()

briAfif.debit(600)
briAfif.kredit(5000)
briAfif.cetakSaldo()

