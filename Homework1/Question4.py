sayi1=12 
sayi2=60 
toplam=0
if sayi1 <= sayi2:
    if sayi1 % 2 == 0: 
        sayi1 = sayi2
        toplam=sayi1+sayi2 
    else: toplam=sayi2-sayi1 
toplam += toplam 
print(toplam)
# sayı 1, sayı2'den küçükse ve sayı1 2'ye tam bölünüyorsa sayı1 ve sayı2 eşitleyip topla ve koşullu ifadenin dışında toplamı kendisi ile bir daha topla ve toplamı çıktı olarak konsola yaz. else koşulu çalışmadı.  Kodun çıktısı = 240