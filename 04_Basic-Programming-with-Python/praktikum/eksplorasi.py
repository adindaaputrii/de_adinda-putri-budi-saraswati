def cek_anagram(kata1, kata2):
    # menghilangkan spasi dan mengubah huruf jadi lowercase
    kata1 = kata1.replace(" ", "").lower()
    kata2 = kata2.replace(" ", "").lower()

    # cek panjang kedua kata
    if len(kata1) != len(kata2):
        return "Bukan Anagram"

    # hitung frekuensi huruf di kata1
    frekuensi_kata1 = {}
    for huruf in kata1:
        if huruf in frekuensi_kata1:
            frekuensi_kata1[huruf] += 1
        else:
            frekuensi_kata1[huruf] = 1

    # hitung frekuensi huruf di kata2
    frekuensi_kata2 = {}
    for huruf in kata2:
        if huruf in frekuensi_kata2:
            frekuensi_kata2[huruf] += 1
        else:
            frekuensi_kata2[huruf] = 1

    # cek frekuensi huruf di kedua kata sama atau tidak
    if frekuensi_kata1 == frekuensi_kata2:
        return "Anagram"
    else:
        return "Bukan Anagram"

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

print(cek_anagram(kata1, kata2))
