from insan import Insan
from issiz import Issiz
from calisan import Calisan
from maviyaka import MaviYaka
from beyazyaka import BeyazYaka
import pandas as pd
class Main:
    try:
        # İnsan sınıfı için nesneler
        insan1 = Insan("12345678901", "Dila", "Kemer", 30, "Kadın", "Türk")
        insan2 = Insan("98765432109", "Ayşenur", "Baysel", 25, "Kadın", "Türk")
        print("\ninsan sınıfı:")
        print(insan1)
        print(insan2)

        # İşsiz sınıfı için nesneler
        issiz1 = Issiz("4185455421", "Sedat", "Kaya", 35, "Erkek", "Türk",24)
        issiz2 = Issiz("278451256", "Can", "Yılmaz", 40, "Erkek", "Türk",83)
        issiz3 = Issiz("414852333", "Eren", "Kuyucu", 28, "Erkek", "Türk",66)
        print("\nişsiz sınıfı:")
        print(issiz1)
        print(issiz2)
        print(issiz3)

        # Çalışan sınıfı için nesneler
        calisan1 = Calisan("486120244", "Halit", "Kara", 30, "Erkek", "Türk", "Bilişim", 59, 5000)
        calisan2 = Calisan("2365987415", "Çağatay", "Argun", 35, "Erkek", "Türk", "Muhasebe", 36, 8000)
        calisan3 = Calisan("69874563256", "Sibel", "Güngör", 28, "Kadın", "Türk", "Satış", 63, 4000)
        print("\nçalışan sınıfı:")
        print(calisan1)
        print(calisan2)
        print(calisan3)

        # Mavi Yaka sınıfı için nesneler
        maviyaka1 = MaviYaka("954623157", "Elif", "Yel", 25, "Kadın", "Türk", "Üretim", 42, 3500, 1000)
        maviyaka2 = MaviYaka("9632587456", "Berk", "Can", 30, "Erkek", "Türk", "Tekstil", 67, 4000, 1500)
        maviyaka3 = MaviYaka("7536951489", "Ahmet", "Güven", 35, "Erkek", "Türk", "Finans", 29, 3000, 800)
        print("\nmaviyaka sınıfı:")
        print(maviyaka1)
        print(maviyaka2)
        print(maviyaka3)

        # Beyaz Yaka sınıfı için nesneler
        beyazyaka1 = BeyazYaka("3984652171", "Canan", "Çelebi", 28, "Kadın", "Türk", "Kalite", 74, 6000, 2000)
        beyazyaka2 = BeyazYaka("2298654715", "Ömer", "İnen", 32, "Erkek", "Türk", "İnsan Kaynakları", 41, 5000, 1200)
        beyazyaka3 = BeyazYaka("1698524793", "Burak", "İplikçi", 30, "Erkek", "Türk", "Pazarlamacı", 98, 8000, 2500)
        print("\nbeyazyaka sınıfı:")
        print(beyazyaka1)
        print(beyazyaka2)
        print(beyazyaka3)

        # Verileri içeren DataFrame oluşturma
        df = pd.DataFrame({
            "nesne_degeri": ["Çalışan", "Çalışan", "Çalışan", "Mavi Yaka", "Mavi Yaka", "Mavi Yaka", "Beyaz Yaka", "Beyaz Yaka", "Beyaz Yaka"],
            "tc_no": [calisan1.get_tc_no(), calisan2.get_tc_no(), calisan3.get_tc_no(), maviyaka1.get_tc_no(), maviyaka2.get_tc_no(), maviyaka3.get_tc_no(), beyazyaka1.get_tc_no(), beyazyaka2.get_tc_no(), beyazyaka3.get_tc_no()],
            "ad": [calisan1.get_ad(), calisan2.get_ad(),calisan3.get_ad(), maviyaka1.get_ad(), maviyaka2.get_ad(), maviyaka3.get_ad(), beyazyaka1.get_ad(), beyazyaka2.get_ad(),beyazyaka3.get_ad() ],
            "soyad": [calisan1.get_soyad(), calisan2.get_soyad(),calisan3.get_soyad(),maviyaka1.get_soyad(), maviyaka2.get_soyad(), maviyaka3.get_soyad(), beyazyaka1.get_soyad(), beyazyaka2.get_soyad(), beyazyaka3.get_soyad()],
            "yas": [calisan1.get_yas(), calisan2.get_yas(), calisan3.get_yas(), maviyaka1.get_yas(), maviyaka2.get_yas(), maviyaka3.get_yas(), beyazyaka1.get_yas(), beyazyaka2.get_yas(), beyazyaka3.get_yas()],
            "cinsiyet": [calisan1.get_cinsiyet(), calisan2.get_cinsiyet(), calisan3.get_cinsiyet(), maviyaka1.get_cinsiyet(), maviyaka2.get_cinsiyet(), maviyaka3.get_cinsiyet(), beyazyaka1.get_cinsiyet(), beyazyaka2.get_cinsiyet(),beyazyaka3.get_cinsiyet()],
            "uyruk": [calisan1.get_uyruk(), calisan2.get_uyruk(), calisan3.get_uyruk(), maviyaka1.get_uyruk(), maviyaka2.get_uyruk(), maviyaka3.get_uyruk(), beyazyaka1.get_uyruk(),beyazyaka2.get_uyruk(),beyazyaka3.get_uyruk() ],
            "sektor": [calisan1.get_sektor(), calisan2.get_sektor(), calisan3.get_sektor(), maviyaka1.get_sektor(),maviyaka2.get_sektor(),maviyaka3.get_sektor(), beyazyaka1.get_sektor(),beyazyaka2.get_sektor(), beyazyaka3.get_sektor()],
            "tecrube": [calisan1.get_tecrube(), calisan2.get_tecrube(), calisan3.get_tecrube(), maviyaka1.get_tecrube(), maviyaka2.get_tecrube(), maviyaka3.get_tecrube(), beyazyaka1.get_tecrube(), beyazyaka2.get_tecrube(), beyazyaka3.get_tecrube()],
            "maas": [calisan1.get_maas(), calisan2.get_maas(), calisan3.get_maas(), maviyaka1.get_maas(), maviyaka2.get_maas(), maviyaka3.get_maas(), beyazyaka1.get_maas(), beyazyaka2.get_maas(), beyazyaka3.get_maas()],
            "yipranma_payi": [0, 0, 0, maviyaka1.get_yipranma_payi(), maviyaka2.get_yipranma_payi(), maviyaka3.get_yipranma_payi(), 0,0,0],
            "tesvik_primi": [0, 0, 0, 0, 0,0, beyazyaka1.get_tesvik_primi(), beyazyaka2.get_tesvik_primi(), beyazyaka3.get_tesvik_primi()],
            "yeni_maas": [calisan1.zam_hakki()+calisan1.get_maas(), calisan2.zam_hakki()+calisan2.get_maas(),calisan3.zam_hakki()+ calisan3.get_maas(), maviyaka1.zam_hakki()+maviyaka1.get_maas(), maviyaka2.zam_hakki()+maviyaka2.get_maas(),maviyaka3.zam_hakki()+maviyaka3.get_maas(), beyazyaka1.zam_hakki()+beyazyaka1.get_maas(), beyazyaka2.zam_hakki()+beyazyaka2.get_maas(),  beyazyaka3.zam_hakki()+beyazyaka3.get_maas()]})




        # Değişken değerlerini 0 olarak ata
        df.fillna(0)

        #Çalışan, Mavi Yaka ve Beyaz Yaka için tecrübe ve yeni maaş ortalamalarını hesaplama
        print("\n1)Çalışan,Maviyaka ve Beyazyakalıların tecrübe ve yeni maaşlarının ortalamaları:\n")
        grup = df.groupby("nesne_degeri").agg({"tecrube": "mean", "yeni_maas": "mean"})
        print(grup)

        # Maaşı 15bin üzerinde olanların sayısını bulma
        maas_ust_limit = 15000
        maas_ust_limit_count = len(df[df["maas"] > maas_ust_limit])
        print("\nMaaşı 15000 TL üzerinde olanların sayısı:", maas_ust_limit_count)

        # Yeni maaşa göre DataFrame'i küçükten büyüğe sıralama
        print("\nYeni maaş sıralamaları:")
        siralama = df.sort_values("yeni_maas")
        print(siralama)

        #Tecrübesi 3 yıldan fazla olan Beyaz yakalıları bulma
        beyazyaka_tecrube_limit = 36
        print("Tecrübesi 3 seneden fazla olan Beyazyakalılar:")
        beyazyaka_tecrube_ust = df[(df["nesne_degeri"] == "Beyaz Yaka") & (df["tecrube"] > beyazyaka_tecrube_limit)]
        print(beyazyaka_tecrube_ust)

        # Yeni maaşı 10bin üzerinde olanlar için 2-5 satır arasındakileri tc_no ve yeni_maaş sütunlarını seçerek gösterme
        yeni_maas_limit = 10000
        print("\nYeni maaşı 10bin üzerindekilerin(2-5 arasındakiler) tc ve yeni maaşları:")
        yeni_maas_ust = df[df["yeni_maas"] > yeni_maas_limit]
        secili_sutunlar= yeni_maas_ust[["tc_no", "yeni_maas"]].iloc[2:5]
        print(secili_sutunlar)

        # yeni bir DataFrame elde etme
        print("\nTüm sektördekilerin ad soyad ve maaşlarını içeren DataFrame:")
        new_df = df[["ad", "soyad", "sektor", "yeni_maas"]]
        new_df.to_string()#noktaları silmek için
        print(new_df)
    except Exception as e:
        print("Bir hata oluştu:", str(e))
