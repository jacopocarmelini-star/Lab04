class Passeggero:
    def __init__(self, codice, nome, cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome
        self.assegnato = False
        self.cabina = None

    def __str__(self):
        stato = "Assegnato" if self.assegnato else "Non assegnato"
        if self.cabina:
            return f"Codice passeggero: {self.codice}, Nome: {self.nome}, Cognome: {self.cognome}, Stato: {stato}, Cabina: {self.cabina}"
        else:
            return f"Codice passeggero: {self.codice}, Nome: {self.nome}, Cognome: {self.cognome}, Stato: {stato}"