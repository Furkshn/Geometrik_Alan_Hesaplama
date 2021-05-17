


#  ------------------ Geometrik Alan Hesaplama Programı ------------------


def geoemetrik_hesaplama():


    print("Geometrik Alan Hesaplama Programına Hoşgeldiniz! ")
    print("\n")
    print("Hesaplamak istediğiniz geometrik şekil belirtiniz")
    print("\n")

    sekil = input(f"""Geometrik Alan Hesabı Yapabilmek İçin Lütfen Geometrik Şekil Seçiniz

        - Dörtgen
        --- Üçgen
                    Hesaplamak İstediğiniz Geometrik Şekil:""")

    if sekil == "dörtgen" or sekil == "Dörtgen":

        dörtgen_tipi = str(input(f"""Seçebileceğiniz dörtgen tipleri:
                    - Kare
                    - Diktdörtgen

Dörtgen Tipi:"""))


        if dörtgen_tipi == "kare" or dörtgen_tipi == "Kare":
            sayı1 = int(input("Lütfen Karenin Kenar Uzunluğunu Giriniz:"))

            karealan = pow(sayı1, 2)

            print("Hesaplamak istediğiniz karenin alanı {}'dır.".format(karealan))

        elif dörtgen_tipi == "diktörgen" or dörtgen_tipi == "Diktörgen":

            sayı2 = int(input("Lütfen Kısa Kenar Değerini Giriniz:"))
            sayı3 = int(input("Lütfen Uzun Kenar Değerini Giriniz:"))

            diktörgenalan = sayı2 * sayı3

            print("Hesaplamak istediğiniz diktörgenin alanı {}'dır.".format(diktörgenalan))

        else:

            print(f"Lütfen Geçerli Dörtgen Tipi Giriniz !")


    elif sekil == "üçgen" or sekil == "Üçgen":

        b = int(input("Lütfen Üçgenin Taban Uzunluk Değerini Giriniz:"))
        h = int(input("Lütfen Üçgenin Yükseklik Değerini Giriniz:"))

        üçgenalan = 0.5 * (b * h)

        print("Hesaplamak istediğiniz üçgenin alanı {}'dır.".format(üçgenalan))

    else:

        print("!!! Program Yalnızca Dörtgen ve Üçgen Alanlarını Hesaplayabilmektedir. !!!")


geoemetrik_hesaplama()