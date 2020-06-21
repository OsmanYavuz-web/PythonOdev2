def DikdortgenAlanCevreHesapla():
    uzun_kenar = int(input("Uzun kenarı girin:"))
    kisa_kenar = int(input("Kısa kenarı girin:"))
    alan =  uzun_kenar * kisa_kenar
    cevre = (uzun_kenar * 2) + (kisa_kenar * 2)
    print ("Alanı: ", alan)
    print ("Çevresi: ", cevre )

while True:
  DikdortgenAlanCevreHesapla();