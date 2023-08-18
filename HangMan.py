import random

Kelimeler = ["elma", "armut", "iskelef", "Nuriye","Afaki", "Açlık", "Abiye", "Abbas", "Balon", "Bahri", "Bahçe", "Cacık", "Camcı", "Cıbıl", 
             "Cümle", "Çöpçü","Çürük", "Çinli", "Çinko", "Çözüm", "Dilim", "Daimi", "Dilek", "Dışkı", "Ezber", "Evlat", "Enfes", "Fosil", 
             "Felek", "Gayet","Giyim", "Gazoz", "Hamak", "Hoşaf", "Hamsi", "İnmek", "İnkar", "İbraz", "Irkçı", "Ilgaz", "Jokey", "Jarse", 
             "Kredi", "Kalın", "Kablo", "Lüzum", "Lotus", "Leğen", "Mevla", "Masal", "Melez", "Nişan", "Nalan", "Ninni", "Oğlak", "Övmek",
             "Ördek", "Pilot", "Posta","Amatör", "Antika", "Adliye", "Bakkal", "Balkon", "Beceri", "Cazibe", "Coşkun", "Çakmak", "Çeviri",
             "Demlik", "Defter", "Devlet", "Emekli", "Elveda", "Fiziki", "Formül", "Fosfor", "Galeri", "Galeta", "Gömlek", "Hayvan", "Haylaz",
             "Hırsız", "İbadet", "İkilem", "İlişki", "Izgara", "Jakuzi", "Kanepe", "Kangal", "Karpuz", "Kısmet", "Lastik", "Medeni", "Makbuz",
             "Alerjik", "Alkolik", "Arınmak", "Boşanma", "Bilmece", "Börülce", "Ciğerci", "Camekan", "Cezaevi", "Çelişki", "Çeşnici", "Demleme",
             "Denizci", "Diriliş", "Eğitmen", "Egzotik", "Emlakçı", "Felaket", "Fabrika", "Genelge", "Gırtlak", "Haziran", "Hipotez", "İtfaiye",
             "astronot", "antoloji", "arkeolog", "atmosfer", "baloncuk", "biyoloji", "biyografi", "bostancı", "bozuşmak", "karbonat", "komplike"]


with open("kelimeler.txt", "w") as dosya:
    for kelime in Kelimeler:
        dosya.write(kelime + "\n")

with open("kelimeler.txt", "r") as dosya:
    satirlar = dosya.readlines()
    rastgele_kelime = random.choice(satirlar).strip()


import turtle

t = turtle.Turtle()
      
t.left(45)         
t.forward(100)    
t.right(90)        
t.forward(100)       
t.backward(100)                 
t.left(135)
t.forward(100*2)
t.left(90)
t.forward(100)
t.left(90)
t.forward(10)

    
def hangMan():
    kelime = random.choice(Kelimeler).strip().lower()
    gizlenmis_kelime = "_" * len(kelime)
    print(gizlenmis_kelime)

    islem = int(input("\nTahmin etmek için 1'e basın\nHarf söylemek için 2'ye basın\n"))

    if islem == 2:
        sayac=0
        while "_" in gizlenmis_kelime:
            
            harf = input("Bir harf girin: ").strip().lower()
            if len(harf) != 1 or not harf.isalpha():
                print("Geçerli bir harf girmelisiniz.")
                continue

            if harf in kelime:
                for i in range(len(kelime)):
                    if kelime[i] == harf:
                        gizlenmis_kelime = gizlenmis_kelime[:i] + harf + gizlenmis_kelime[i+1:]
                        print("Gizli kelime:", gizlenmis_kelime)
                        
                        print("Tahminde Bulunmak ister misiniz?\nevet = 1\nhayır = 2")
                        karar=int(input())
                        if karar == 1:
                            tahmin2 = input("Tahmininiz nedir = ")
                            if tahmin2.lower() == kelime:
                                 print(f"Tebrikler! Doğru tahmin ettiniz. Cevap = {kelime}")
                            else:
                                  print(f"Maalesef yanlış. Doğru cevap = {kelime}")
                                  print("Program sonlandırılıyor....")
            else:
                sayac+=1
                print("Girilen harf kelimenin içinde yok.")
                if sayac ==1:
                    
                    t.penup()
                    t.right(45)
                    t.forward(30)
                    t.pendown()
                    t.circle(30)       
                    t.left(90)
                    t.penup()
                    t.forward(30)
                    t.right(45)
                    t.forward(30)
                    t.pendown()
                elif sayac ==2:
                    t.forward(60)        
                    t.backward(50)
                elif sayac ==3:
                    t.right(45)
                    t.forward(30)         
                    t.backward(30)
                    t.left(45)
                elif sayac==4:
                    t.left(45)
                    t.forward(30)    
                    t.backward(30)
                    t.right(45)
                    t.forward(60)
                elif sayac==5:
                    t.right(45)
                    t.forward(30)   
                    t.backward(30)
                    t.left(45)
                else:
                    t.left(45)         
                    t.forward(30)
                    print("Son tahmin hakkınızı kullandırınız ")
                    print(f"Doğru cevap {kelime}")
                    break
    elif islem == 1:
        tahmin = input("Tahmininiz nedir = ")
        if tahmin.lower() == kelime:
            print(f"Tebrikler! Doğru tahmin ettiniz. Cevap = {kelime}")
        else:
            print(f"Maalesef yanlış. Doğru cevap = {kelime}")
            print("Program sonlandırılıyor....")

hangMan()
