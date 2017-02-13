from personaggio import Personaggio

class Saiyan(Personaggio):
    def __init__(self, nome, forza, aura, salute):
        Personaggio.__init__(self, nome, forza, aura, salute)
        Personaggio.trasformazine = True

    def __str__(self):
        return "Saiyan \n" + Personaggio.__str__(self)
