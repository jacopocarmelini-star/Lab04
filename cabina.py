class Cabina:
    def __init__(self, codice, letti, ponte, prezzo):
        self.codice = codice
        self.letti = letti
        self.ponte = ponte
        self.prezzo = prezzo



class CabinaAnimali:
    def __init__(self, codice, letti, ponte, prezzo, animali):
        super().__init__(codice, letti, ponte, prezzo)
        self._prezzo_iniziale = prezzo
        self.animali = animali

    @property
    def prezzo(self):
        return self._prezzo_iniziale * (1 + 0.10*self.animali)
    @prezzo.setter
    def prezzo(self, nuovo_prezzo):
        self._prezzo_iniziale = nuovo_prezzo


class CabinaDeluxe:
    def __init__(self, codice, letti, ponte, prezzo, stile):
        super().__init__(codice, letti, ponte, prezzo)
        self.stile = stile
        self._prezzo_iniziale = prezzo

    @property
    def prezzo(self):
        return self._prezzo_iniziale * 1.20
    @prezzo.setter
    def prezzo(self, nuovo_prezzo):
        self._prezzo_iniziale = nuovo_prezzo