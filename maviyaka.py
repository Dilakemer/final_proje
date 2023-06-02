from calisan import Calisan
#MaviYaka sınıfını oluştur.
class MaviYaka(Calisan):
    #initilaizer metot ile değişkenleri private ata.
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__yipranma_payi = yipranma_payi
#getter ve setter metotu
    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi
#zam_hakkı nı tecrübeye göre hesaplayan metot
    def zam_hakki(self):
        try:
            if self.get_tecrube() < 24:
                zam_orani = self.__yipranma_payi * 10
            elif 24 <= self.get_tecrube() < 48 and self.get_maas() < 15000:
                zam_orani = (self.get_maas() % self.get_tecrube()) / 2 + self.__yipranma_payi * 10
            elif self.get_tecrube() >= 48 and self.get_maas() < 25000:
                zam_orani = (self.get_maas() % self.get_tecrube()) / 3 + self.__yipranma_payi * 10
            else:
                zam_orani = 0

            yeni_maas = self.get_maas() + zam_orani
            if yeni_maas == self.get_maas():
                return self.get_maas()
            else:
                self.set_maas(yeni_maas)
                return yeni_maas
        except Exception as e:
            print("Bir hata oluştu:", str(e))
#str metotu ile ekrana yaz.
    def __str__(self):
        return f"{super().__str__()}\nYıpranma Payı: {self.__yipranma_payi}\nYeni Maaş: {self.zam_hakki()}"
