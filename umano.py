from personaggio import Personaggio

class Umano(Personaggio):
    def __init__(self, nome, forza, aura, salute):
        Personaggio.__init__(self, nome, forza, aura, salute)
    
    def __str__(self):
        return "Umano \n" + Personaggio.__str__(self)
