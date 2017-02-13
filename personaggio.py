class Personaggio:
    def __init__(self, nome, forza, aura, salute):
            self.nome = nome
            self.forza = forza
            self.aura = aura
            self.salute = salute
            self.trasformazione = False
    def __str__(self):
            return "Nome: " + self.nome + "\n" + \
                    "Forza: " + str(self.forza) + "\n" + \
                    "Aura: " + str(self.aura) + "\n" + \
                    "Salute: " + str(self.salute) + "\n" + \
                    "Trasformazione: " + str(self.trasformazione) + "\n"
