class Passeggero:
    def __init__(self, codice, nome, cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome

    def __str__(self):
        return f"Codice passeggero: {self.codice}, Nome: {self.nome}, Cognome: {self.cognome}"