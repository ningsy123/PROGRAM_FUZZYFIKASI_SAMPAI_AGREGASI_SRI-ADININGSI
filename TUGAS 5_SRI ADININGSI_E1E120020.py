import sys
import numpy as np
import matplotlib.pyplot as plt
import math

print('NAMA \t: SRI ADININGSI')
print('NIM \t: E1E120020')
print('PROGRAM MENENTUKAN FUNGSI INTERVASI FUZZY')

print('\nDiketahui :')
print('Permintaan Terbesar = 5000')
print('Permintaan Terkecil = 1000')
print('Persediaan Terbanyak = 600')
print('Persediaan Terkecil = 100')
print('Produksi Barang Berkurang = 7000')
print('Produksi Barang Bertambah = 2000 \n')

print('Pertanyaan : ')
minta = float(input('Masukkan  Jumlah Permintaan = '))
sedia = float(input('Masukkan Jumlah Persediaan = '))

print('\n1. Fuzzyfikasi')


def permintaan_turun(minta):
    if minta <= 1000:
        return 1.0
    elif minta >= 5000:
        return 0.0
    else:
        return (5000 - minta) / (5000 - 1000)


def permintaan_naik(minta):
    if minta <= 1000:
        return 0.0
    elif minta >= 5000:
        return 1.0
    else:
        return (minta - 1000) / (5000 - 1000)


def persediaan_turun(sedia):
    if sedia <= 100:
        return 1.0
    elif sedia >= 600:
        return 0.0
    else:
        return (600 - sedia) / (600 - 100)


def persediaan_naik(sedia):
    if sedia <= 100:
        return 0.0
    elif sedia >= 600:
        return 1.0
    else:
        return (sedia - 100) / (600 - 100)


def produksi_brg_turun(produksi):
    if produksi <= 2000:
        return 1.0
    elif produksi >= 7000:
        return 0.0
    else:
        return (7000 - produksi) / (7000-2000)


def produksi_brg_naik(produksi):
    if produksi <= 2000:
        return 0.0
    elif produksi >= 7000:
        return 1.0
    else:
        return (produksi - 2000) / (7000-2000)


# permintaan turun
print('Nilai derajat keanggotaan permintaan turun = ', permintaan_turun(minta))
x = np.linspace(0, 5000+50, 10000)
y = [permintaan_turun(i) for i in x]
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Keanggotaan')
plt.title('Fungsi Keanggotaan Permintaan Turun')
if minta < 0 or minta > 10000:
    print("Nilai x harus antara 0 dan 10000")
else:
    y_input = permintaan_turun(minta)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.axvline(x=minta, color='b', linestyle='--')
    plt.axhline(y=y_input, color='b', linestyle='--')
####################

# permintaan naik
print('Nilai derajat keanggotaan permintaan naik = ', permintaan_naik(minta))
x = np.linspace(0, 5000+50, 10000)
y = [permintaan_naik(i) for i in x]
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Keanggotaan')
plt.title('Fungsi Keanggotaan Permintaan Naik')
if minta < 0 or minta > 10000:
    print("Nilai x harus antara 0 dan 10000")
else:
    y_input = permintaan_naik(minta)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('Derajat Keanggotaan')
    plt.title('Fungsi Keanggotaan Permintaan Naik dan Turun')
    plt.axvline(x=minta, color='b', linestyle='--')
    plt.axhline(y=y_input, color='b', linestyle='--')
plt.show()
####################

# persediaan turun
print('Nilai derajat keanggotaan persediaan turun = ', persediaan_turun(sedia))
x = np.linspace(0, 600+50, 10000)
y = [persediaan_turun(i) for i in x]
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Keanggotaan')
plt.title('Fungsi Keanggotaan Permintaan Turun')
if sedia < 0 or sedia > 10000:
    print("Nilai x harus antara 0 dan 10000")
else:
    y_input = persediaan_turun(sedia)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.axvline(x=sedia, color='b', linestyle='--')
    plt.axhline(y=y_input, color='b', linestyle='--')
#############

# persediaan naik
print('Nilai derajat keanggotaan persediaan naik = ', persediaan_naik(sedia))
x = np.linspace(0, 600+50, 10000)
y = [persediaan_naik(i) for i in x]
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Keanggotaan')
plt.title('Fungsi Keanggotaan Permintaan Naik')
if sedia < 0 or sedia > 10000:
    print("Nilai x harus antara 0 dan 10000")
else:
    y_input = persediaan_naik(sedia)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('Derajat Keanggotaan')
    plt.title('Fungsi Keanggotaan Persediaan Terkecil dan Terbanyak')
    plt.axvline(x=sedia, color='b', linestyle='--')
    plt.axhline(y=y_input, color='b', linestyle='--')
plt.show()
####################

# Produksi barang turun
x = np.linspace(0, 7000+50, 10000)
y = [produksi_brg_turun(i) for i in x]
plt.plot(x, y)
plt.xlabel('x')
plt.plot(x, y)

# Produksi barang naik
x = np.linspace(0, 7000+50, 10000)
y = [produksi_brg_naik(i) for i in x]
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Derajat Keanggotaan')
plt.title('Fungsi Keanggotaan Produksi Barang Turun dan Naik')
plt.plot(x, y)
plt.show()


print('\n2. Operasi Logika Fuzzy dan')
print('3. Implikasi Kaidah Fuzzy\n')

print('[R1] IF Permintaan TURUN And Persediaan BANYAK THEN Produksi Barang BERKURANG')
nilai_min1 = min(permintaan_turun(minta), persediaan_naik(sedia))
print('(', '', permintaan_turun(minta), ',', '', persediaan_naik(sedia), ')')
print("Nilai minimum adalah", nilai_min1)

print('\n[R2] IF Permintaan TURUN And Persediaan SEDIKIT THEN Produksi Barang BERKURANG')
nilai_min2 = min(permintaan_turun(minta), persediaan_turun(sedia))
print('(', '', permintaan_turun(minta), ',', '', persediaan_turun(sedia), ')')
print("Nilai minimum adalah", nilai_min2)
print('\n[R3] IF Permintaan NAIK And Persediaan BANYAK THEN Produksi Barang BERTAMBAH')
nilai_min3 = min(permintaan_naik(minta), persediaan_naik(sedia))
print('(', '', permintaan_naik(minta), ',', '', persediaan_naik(sedia), ')')
print("Nilai minimum adalah", nilai_min3)
print('\n[R4] IF Permintaan NAIK And Persediaan SEDIKIT THEN Produksi Barang BERTAMBAH')
nilai_min4 = min(permintaan_naik(minta), persediaan_turun(sedia))
print('(', '', permintaan_naik(minta), ',', '', persediaan_turun(sedia), ')')
print("Nilai minimum adalah", nilai_min4)

print('\n4. Agregasi')
print('---Fungsi Max Grafik Berkurang dan Bertambah---')
print('(', '', nilai_min1, ',', '', nilai_min2, ')')
nilai_max1 = max(nilai_min1, nilai_min2)
print("Nilai Maximum Berkurang adalah", nilai_max1)
print('(', '', nilai_min3, ',', '', nilai_min4, ')')
nilai_max2 = max(nilai_min3, nilai_min4)
print("Nilai Maximum Bertambah adalah", nilai_max2)

print("\n---Mencari Nilai a1 dan a2---")
if nilai_max1 > nilai_max2:
    z1 = 7000 - (5000*nilai_max1)
    print("Nilai a1 adalah ", z1)
    z2 = 7000 - (5000*nilai_max2)
    print("Nilai a2 adalah ", z2)

    print("\n---Fungsi keanggotaan hasil komposisi ini adalah---")
    print(" ", nilai_max1, " ; z <= ", z1)
    print("7000-z/5000", " ; ", z1, "<=z<=", z2)
    print(" ", nilai_max2, " ; >= ", z2)

else:
    z1 = (5000*nilai_max1)+2000
    print("Nilai a1 adalah ", z1)
    z2 = (5000*nilai_max2)+2000
    print("Nilai a2 adalah ", z2)

    print("\n---Fungsi keanggotaan hasil komposisi ini adalah---")
    print(" ", nilai_max1, " ; z <= ", z1)
    print("z-2000/5000", " ; ", z1, "<= z <=", z2)
    print(" ", nilai_max2, " ; >= ", z2)
