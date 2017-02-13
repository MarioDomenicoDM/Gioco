from saiyan import Saiyan
from umano import Umano

s=input("1 = Goku || 2 = Crilin\n")
if s==1:
    goku = Saiyan ("Goku", 100, 24000, 100)
    print goku
if s==2:
    crilin = Umano ("Crilin", 30, 20, 100)
    print crilin
if s>2:
    print "ERRORE"
