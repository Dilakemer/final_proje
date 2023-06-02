from insan import Insan
# issiz clasini oluştur.
class Issiz(Insan):
    # initilaizer metot ile değişkenleri private tanımla.
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrubeler):
        # kalıtım ile değişkenleri çağır.
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__tecrubeler = tecrubeler

    # getter ve setter metotları
    def get_tecrubeler(self):
        return self.__tecrubeler

    def set_tecrubeler(self, tecrubeler):
        self.__tecrubeler = tecrubeler

    # statu_bul ile hesaplanan statuyu değişkene atıyoruz.
    def statu_bul(self):
        try:
            etkiler = {
                "mavi_yaka": 0.2,
                "beyaz_yaka": 0.35,
                "yonetici": 0.45
            }

            en_yuksek_etki = max(etkiler.values())
            en_yuksek_statu = None

            for statu, etki in etkiler.items():
                yil = self.__tecrubeler * (1 + etki)
                if etki == en_yuksek_etki:
                    en_yuksek_statu = statu
                elif yil > self.__tecrubeler * (1 + en_yuksek_etki):
                    en_yuksek_statu = statu

            return en_yuksek_statu

        except Exception as e:
            print("Bir hata oluştu:", str(e))
    # str metotu ile ekrana yaz.
    def __str__(self):
        return f"{super().__str__()}\nStatü: {self.statu_bul()}"
