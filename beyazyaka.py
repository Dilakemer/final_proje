from calisan import Calisan
# BeyazYaka sınıfını oluştur
class BeyazYaka(Calisan):
    # initilaizer metot ile değişkenleri private ata.
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvik_primi = tesvik_primi

    # getter ve setter metotları
    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi

    # zam_hakkı nı tecrübeye göre hesaplayan metot
    def zam_hakki(self):
        try:
            if self.get_tecrube() < 24:
                zam_orani = self.__tesvik_primi
            elif 24 <= self.get_tecrube() < 48 and self.get_maas() < 15000:
                zam_orani = (self.get_maas() % self.get_tecrube()) / 2 + self.__tesvik_primi
            elif self.get_tecrube() >= 48 and self.get_maas() < 25000:
                zam_orani = (self.get_maas() % self.get_tecrube()) * 4 + self.__tesvik_primi
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
    # str ile ekrana yaz.
    def __str__(self):
        return f"{super().__str__()}\nTeşvik Prim: {self.__tesvik_primi}\nYeni Maaş: {self.zam_hakki()}"
