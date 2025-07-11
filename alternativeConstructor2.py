class gamer:
    associationName="Kakas Squad"
    def __init__(self,name,game,salary):
        self.name=name
        self.game=game
        self.salary=salary
    def showInfo(self):
        print(f"Name of the gamer is {self.name}. He plays {self.game} and his salary:{self.salary}")
        print(f"{self.name} plays for {self.associationName}")
    @classmethod
    def convert(cls,string):
        return cls(string.split("-")[0],string.split("-")[1],int(string.split("-")[2]))
g1=gamer("Abrar","Efootball",20000)
g1.showInfo()
string1="Anik-Arena of Valor-18000"
string2="Akib-PUBG Mobile-22000"
g2=gamer.convert(string1)
g2.showInfo()
g3=gamer.convert(string2)
g3.showInfo()
