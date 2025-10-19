import csv
from passeggero import Passeggero
from cabina import *

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self._nome = nome
        self.passeggeri = []
        self.cabine = []

    """Aggiungere setter e getter se necessari"""
    # TODO
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        # TODO
        try:
            with open(file_path,'r', encoding="utf-8" ) as file:
                reader = csv.reader(file)
                for riga in reader:
                    if len(riga) < 4:
                        passeggero = Passeggero(riga[0], riga[1], riga[2])
                        self.passeggeri.append(passeggero)
                    elif len(riga) ==4:
                        cabina_standard = Cabina(riga[0], int(riga[1]), int(riga[2]), int(riga[3]))
                        self.cabine.append(cabina_standard)
                    elif len(riga) > 4 :
                        if riga[4].isdigit():
                            # CabinaAnimali
                            cabina = CabinaAnimali(riga[0], int(riga[1]), int(riga[2]), int(riga[3]), int(riga[4]))
                        else:
                            # CabinaDeluxe
                            cabina = CabinaDeluxe(riga[0], int(riga[1]), int(riga[2]), int(riga[3]), riga[4])
                        self.cabine.append(cabina)


        except FileNotFoundError:
            raise FileNotFoundError("File non trovato")



    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO
        passeggero = None
        for p in self.passeggeri:
            if p.codice == codice_passeggero:
                passeggero = p
        if passeggero is None:
            raise Exception("Passeggero non trovato")
        elif passeggero.assegnato:
            raise Exception("Passeggero già assegnato")

        cabina = None
        for c in self.cabine:
            if c.codice == codice_cabina:
                cabina = c
        if cabina is None:
            raise Exception("Cabina non trovata")
        elif cabina.prenotata:
            raise Exception("Cabina già occupata")

        passeggero.assegnato = True
        passeggero.cabina = codice_cabina
        cabina.prenotata = True

        print(f"Passeggero {passeggero.codice} assegnato alla cabina {cabina.codice}.")

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO
        return sorted(self.cabine, key=lambda c:c.prezzo)

    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO
        for passeggero in self.passeggeri:
            print(passeggero)
