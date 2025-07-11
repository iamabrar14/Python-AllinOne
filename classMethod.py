"""
In Python, a class method is a method that is bound to the class and not the instance of the class. 
It can access and modify class state that applies across all instances of the class.
@classmethod is used to define a class method. It takes the class (cls) as its first parameter.
"""

class Game:
    gameName = "Efootball"

    def __init__(self, name):
        self.name = name

    def showGamer(self):
        print(f"Name of the gamer is {self.name} and he plays {self.gameName}")

    @classmethod
    def changeGame(cls, Newgame):
        cls.gameName = Newgame

# Creating first gamer
o = Game("Abrar")
o.showGamer()

# Changing name of the game using class method
Game.changeGame("PUBG Mobile")

# Creating second gamer
o2 = Game("Akib")
o2.showGamer()
