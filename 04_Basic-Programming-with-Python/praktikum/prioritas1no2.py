print("Menghitung Volume Bola")
jari_jari = float(input("Masukkan nilai jari-jari: "))

if jari_jari % 7 == 0:
    phi = 22/7
else:
    phi = 3.14

volume = 4/3 * phi * jari_jari**3

print("Volume bola adalah", volume)