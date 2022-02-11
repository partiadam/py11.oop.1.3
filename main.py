'''
1.3 Feladat
Készíts egy programot, amelyben van egy Negyzet nevű osztály. Attribútuma legyen az oldal hossza. Rendelkezzen továbbá a kerület és terület számításra is egy-egy metódussal!

Készíts egy programot, amely a felhasználótól egymás után bekéri a négyzetek oldalhosszát egészen addíg, amíg a felhasználó 0 értéket nem ad meg! Ezen adat alapján a program hozzon létre negyzet objektumokat, melyeket egy listában tárol! A program írja ki a megadott négyzetek oldalhosszát, kerületét és területét!
'''

lista = []
class Negyzet:
    def __init__(self, oldalhossz):
        self.oldalhossz = oldalhossz
    def terulet(self):
        return self.oldalhossz ** 2

    def kerulet(self):
        return self.oldalhossz * 4 
    
while True:
        beker = input('Négyzet oldal hossza: ')
        if beker == "" or beker == str(0):
            break
        lista.append(int(beker))
for i in lista:
    negyzet1 = Negyzet(i)
        
    print(f"A négyzet kerülete {negyzet1.kerulet()}, a területe {negyzet1.terulet()}")
        