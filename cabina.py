class Cabina:
    def __init__(self, codice, letti, ponte, prezzo):
        self.codice = codice
        self.letti = letti
        self.ponte = ponte
        self.prezzo = prezzo
        self.prenotata = False

    def __str__(self):
        stato = "Prenotata" if self.prenotata else "Disponibile"
        return f"Codice: {self.codice}, Letti: {self.letti}, Ponte: {self.ponte}, Prezzo: {self.prezzo:.2f}€, Disponibilità: {stato}"


class CabinaAnimali(Cabina):
    def __init__(self, codice, letti, ponte, prezzo, animali):
        super().__init__(codice, letti, ponte, prezzo)
        self._prezzo_base = prezzo
        self.animali = animali

    def __str__(self):
        stato = "Prenotata" if self.prenotata else "Disponibile"
        return f"Codice: {self.codice}, Letti: {self.letti}, Ponte: {self.ponte}, Prezzo: {self.prezzo:.2f}€, Animali: {self.animali}, Disponibilità: {stato}"

    @property
    def prezzo(self):
        return self._prezzo_base * (1 + 0.10*self.animali)
    @prezzo.setter
    def prezzo(self, nuovo_prezzo):
        self._prezzo_base = nuovo_prezzo


class CabinaDeluxe(Cabina):
    def __init__(self, codice, letti, ponte, prezzo, stile):
        super().__init__(codice, letti, ponte, prezzo)
        self.stile = stile
        self._prezzo_base = prezzo

    @property
    def prezzo(self):
        return self._prezzo_base * 1.20
    @prezzo.setter
    def prezzo(self, nuovo_prezzo):
        self._prezzo_base = nuovo_prezzo

    def __str__(self):
        stato = "Prenotata" if self.prenotata else "Disponibile"
        return f"Codice: {self.codice}, Letti: {self.letti}, Ponte: {self.ponte}, Prezzo: {self.prezzo:.2f}€, Stile: {self.stile}, Disponibilità: {stato}"
