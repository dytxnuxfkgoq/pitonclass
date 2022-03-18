class Diak():
    def __init__(self,vnev,knev,pont):
        self.vnev = vnev
        self.knev = knev
        self.pont = pont
    def __repr__(self):
        return f"{self.vnev} {self.knev}-nak {self.pont} pontja van a kis faszgecinek"
    def vizsgal(self):
        if self.pont > 20:
            return "átment"
        else:
            return "nem ment át"


diak1 = Diak("Kiss","Lajos",34)
diak2 = Diak("Nagy","Tihamér",11)

print(diak1.vnev,diak1.knev)
print(diak1, diak1.vizsgal())
print(diak2, diak2.vizsgal())

class Auto():
    def __init__(self,tipus,marka,evjarat):
        self.tipus = tipus
        self.marka = marka
        self.evjarat = evjarat
    def __repr__(self):
        return f"Típus: {self.tipus} Márka: {self.marka} Évjárat: {self.evjarat}"
    def autovizsgal(self):
        if self.evjarat < 2010:
            return "Az autó régi évjáratú"
        else:
            return "Az autó új évjáratú"

auto1 = Auto("M5","BMW",2005)
auto2 = Auto("i8","BMW",2013)
print(auto1, auto1.autovizsgal())
print(auto2, auto2.autovizsgal())