class Kalkulator:
    def __init__(self, *nominal):
        self.nominal = nominal

    def dzialanie_grosz(self):
        jdngrsz = int(input("Podaj ilość jednogroszówek: "))
        dwagrsz = int(input("Podaj ilość dwugroszówek: "))
        piecgrsz = int(input("Podaj ilość pięciogroszówek: "))
        dziesgorosz = int(input("Podaj ilość dziesięciogroszówek: "))
        dwadziesgrosz = int(input("Podaj ilość dwudziestogroszówek: "))
        piecdziesgorsz = int(input("Podaj ilość pięćdziesięciogroszówek: "))

        wynik_mnozenia_jdngrsz = jdngrsz * 0.01
        wynik_mnozenia_dwagrsz = dwagrsz * 0.02
        wynik_mnozenia_piecgrsz = piecgrsz * 0.05
        wynik_mnozenia_diesgrosz = dziesgorosz * 0.1
        wynik_mnozenia_dwadziesgrosz = dwadziesgrosz * 0.2
        wynik_mnozenia_piecdziesgrosz = piecdziesgorsz * 0.5

        return round(wynik_mnozenia_jdngrsz, 2), \
            round(wynik_mnozenia_dwagrsz, 2), \
            round(wynik_mnozenia_piecgrsz, 2), \
            round(wynik_mnozenia_diesgrosz, 2), \
            round(wynik_mnozenia_dwadziesgrosz, 2), \
            round(wynik_mnozenia_piecdziesgrosz, 2)

    def dzialanie_zlotowki(self):
        zet = int(input("Podaj ilość złotówek: "))
        dwazet = int(input("Podaj ilość dwuzłotówek: "))
        pieczet = int(input("Podaj ilość pięciozłotówek: "))
        dzieszet = int(input("Podaj ilość dziesięciozłotówek: "))
        dwadzieszet = int(input("Podaj ilość dwudziestozłotówek: "))
        piecdzieszet = int(input("Podaj ilość pięćdziesięciozłotówek: "))
        stozet = int(input("Podaj ilość stuzłotówek: "))
        dwiesciezet = int(input("Podaj ilość dwustuzłotówek: "))

        wynik_mnozenia_zet = zet * 1.00
        wynim_mnozenia_dwazet = dwazet * 2.00
        wynik_mnozenia_pieczet = pieczet * 5.00
        wynik_mnozenia_dzieszet = dzieszet * 10.00
        wynik_mnozenia_dwadzieszet = dwadzieszet * 20.00
        wynik_mnozenia_piecdzieszet = piecdzieszet * 50.00
        wynik_mnozenia_stozet = stozet * 100.00
        wynik_mnozenia_dwiesciezet = dwiesciezet * 200.00

        return round(wynik_mnozenia_zet, 2), \
            round(wynim_mnozenia_dwazet, 2), \
            round(wynik_mnozenia_pieczet, 2), \
            round(wynik_mnozenia_dzieszet, 2), \
            round(wynik_mnozenia_dwadzieszet, 2), \
            round(wynik_mnozenia_piecdzieszet, 2), \
            round(wynik_mnozenia_stozet, 2), \
            round(wynik_mnozenia_dwiesciezet, 2)


# dodaj tutaj funkcję main:

def main():
    while True:
        decyzja = input("Chcesz obliczyć grosze (1), złotówki (2), czy wyjść z programu (0)? ")

        if decyzja == "1":
            oblicz = Kalkulator()
            wynik = oblicz.dzialanie_grosz()
            print(f"Suma groszy (w złotówkach): {wynik}")

        elif decyzja == "2":
            oblicz = Kalkulator()
            wynik = oblicz.dzialanie_zlotowki()
            print(f"Suma złotówek: {wynik}")

        elif decyzja == "0":
            print("Dziękuję, do zobaczenia.")
            break
        
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()
