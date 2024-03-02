print ("Menghitung Luas Persegi Panjang")
panjang = float(input("Masukkan nilai panjang: "))
lebar = float(input("Masukkan nilai lebar: "))

luas = panjang * lebar

if luas % 2 == 0:
    jenis_persegi_panjang = "even rectangle"
else:
    jenis_persegi_panjang = "odd rectangle"

print("Luas persegi panjang adalah", luas)
print("Jenis persegi panjang adalah6", jenis_persegi_panjang)