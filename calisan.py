from insan import Insan
#calisan sınıfını oluştur.
class Calisan(Insan):
#initilaizer metot ile değişkenleri private ata.
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = sektor
        self.__tecrube = tecrube
        self.__maas = maas
#getter ve setter metotları
    def get_sektor(self):
        return self.__sektor

    def set_sektor(self, sektor):
        self.__sektor = sektor

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        self.__maas = maas
#zam_hakkı nı tecrübeye göre hesaplayan metot.
    def zam_hakki(self):
        try:
            if self.__tecrube < 24:
                zam_orani = 0
            elif 24 <= self.__tecrube < 48 and self.__maas < 15000:
                zam_orani = self.__maas % self.__tecrube
            elif self.__tecrube >= 48 and self.__maas < 25000:
                zam_orani = (self.__maas % self.__tecrube) / 2
            else:
                zam_orani = 0

            yeni_maas = self.__maas + zam_orani
            if yeni_maas == self.__maas:
                return self.__maas
            else:
                self.__maas = yeni_maas
                return yeni_maas
        except Exception as e:
            print("Bir hata oluştu:", str(e))
#str metotu ile ekrana yaz.
    def __str__(self):
        return f"{super().__str__()}\nSektör: {self.__sektor}\nTecrübe: {self.__tecrube}\nYeni Maaş: {self.zam_hakki()}"
