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

"""list2 = []
list3 = []
list = ["Anna","Bela","Janos","Karoly","Bladimeri"]
for x in list:
    if len(x) > 5:
        list2.append(x)
    else:
        list3.append(x)
print(list2,list3)"""

"""class Diak():
    def __init__(self,keresztnev,jegy):
        self.keresztnev = keresztnev
        self.jegy = jegy
    def __repr__(self):
        return f"{self.keresztnev} {self.jegy}"
    def jegyvizsgal(self):
        if self.jegy == 1:
            return "megbukott"
        else:
            return "nem bukott meg"
f = open("diakosztalyzat.txt","r",encoding="UTF-8")
list = []
for sor in f:
    s = sor.strip().split()
    print(s)
    keresztnev = s[0]
    jegy = s[1]
    diak=Diak(s[0],int(s[1])) 
    list.append(diak)
print(list)
for i in list:
    print(i, i.jegyvizsgal())"""

class Ajandek():
    def __init__(self,mit,ar):
        self.mit = mit
        self.ar = ar
    def __repr__(self):
        return f"{self.mit} {self.ar}"
f= open("bolt.txt","r",encoding="UTF-8")
list = []
for sor in f:
    sor = sor.strip().split(";")
    aj=Ajandek(sor[0],sor[1])
    list.append(aj)
print(list)
osszeg = 0
for i in list:
    osszeg += i[1]
print(osszeg)
