#from random import randint

clovece = None  # premenna, co zachytava sucasny status

# Trieda reprezentujuca jehu hru clovece
class Clovece(object):
    fig = 4; plocha = 40  # pocet figuriek, velkost plochy

    status = ()

    # Konstruktor vytvori hru s danym poctom hracov z int <2, 6>
    def __init__(self, number = 4 ):
        # Reprezentuje plochu clovece. Hodnoty typu (hrac, figurka)
        clovece = [(-1, -1) for i in range(40)]

        # Ulozime si, na ktorych polickach su jednotlive figurky hracov
        policko = {i: [10*i for j in range(self.fig)] for i in range(number)}

        # Stav plochy, figuriek, pocet hracov, v ktorom kole sme, ktory hrac bol posledne na tahu
        self.status = (clovece, policko, number, 0, 0)

        # Funkcia na detekciu kolizii s inou figurkou
    def kolizia(self, mojaPoloha):
        hrac = self.status[0][mojaPoloha][0]
        figurka = self.status[0][mojaPoloha][1]
        return (hrac, figurka)
        #print("Kolizia s figurkou", figurka, "hraca", hrac)
        #self.status[1][hrac][figurka] = 0  # ak tam uz je figurka, tak ta prva ide na 0

    # Tah jedneho hraca
    def tah(self):
        hrac = self.status[4]
        kolo = self.status[3]
        number = self.status[2]
        policko = self.status[1]
        clovece = self.status[0]

        print("Na tahu je hrac", hrac)
        #hod = randint(1, 6) #hod kocky
        hod = 2
        print("Hodili ste", hod)
        #figurka = -1;

        #while figurka < 0 or figurka >= self.fig:
            #figurka = int(input("Chcem ist figurkou č. (0 - 3): "))  # hrac si vyberie figurku
            #if figurka < 0 or figurka >= self.fig: print("Neplatne cislo figurky!")

        figurka = (hrac + kolo) % 4

        kolizne = self.kolizia(policko[hrac][figurka] + hod)  # riesenie kolizii: druhy vyhrava
        print(kolizne)
        if kolizne[0] == hrac:
            print("Nemozno sa posunut. Na tomto policku uz mate figurku")
        else:
            if kolizne != (-1, -1):
                pomH = kolizne[0]
                pomF = kolizne[1]
                print("Kolizia s figurkou", figurka, "hraca", hrac)
                # ak tam uz je figurka, tak ta prva ide na pociatok
                self.status[1][pomH][pomF] = 10*pomH
            clovece[policko[hrac][figurka]] = (-1, -1) #vyprazdnime to, kde prave bola
            policko[hrac][figurka] += hod  # figurka sa posunie o hodeny pocet policok
            clovece[policko[hrac][figurka]] = (hrac, figurka)  # nova na dane policko
        print()

        if policko[hrac][figurka] >= self.plocha + 10*hrac:
            print("Hrac", hrac, "vyhral. Gratulujeme!")
            exit(0)
        self.status = (clovece, policko, number, kolo, hrac)
        return policko[hrac][figurka]

    def vypis_kolo(self, fin):
        pocet = self.status[2]
        if fin:
            print("Stav hracov po skonceni hry:")
        else: print("Stav hracov pred kolom", str(self.status[3] + 1) + ":")
        for i in range(pocet):
            print("Hrac", i, ":", end=' ')
            for j in range(self.fig):
                print(self.status[1][i][j], end=' ')
            print()
        print("\n")

    def hraj(self):
        global status
        pocet = self.status[2]

        while True:  # kym niekto nevyhra
            self.vypis_kolo(0)
            for hrac in range(pocet):  # tah kazdeho hraca
                self.status = (self.status[0], self.status[1],
                               self.status[2], self.status[3], hrac)
                self.tah()

            self.status = (self.status[0], self.status[1], self.status[2],
                           self.status[3] + 1, self.status[4])

            #inp = input("Ukoncit hru: \'a\'\nPokracovat: lubovolne ine")
            status = self.ziskaj_status()
            #if inp == 'a':
                #print("Rozhodli ste sa ukoncit hru.")
                #self.vypis_kolo(1)
                #exit(0)
            if self.status[3] == 12:
                return (self.status[3], self.status[4])

    def ziskaj_status(self):
        return [self.status[i] for i in range(3)]


# Spyta sa na pocet hracov a vytvori novu hru
def novaHra():
    # Na zaciatku sa spytame na pocet hracov. Ten musi byt z intervalu [1,4]
    #number = 0  # pocet hracov clovece
    #minp = 2
    #maxp = 4
    #while number < minp or number > maxp:
        #number = int(input("Zadajte pocet hracov (" + str(minp) + " - " + str(maxp) + "): "))
        #if number < minp or number > maxp: print("Neplatny pocet hracov!")
    #return Clovece(number)
    return Clovece(4)

if __name__ == "__main__":
    clovece = novaHra()
    clovece.hraj()
