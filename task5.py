class Greeter:
    greeting = "Hello Mam Assalamoalikum!"

    def __init__(self, name,batch):
        self.name = name
        self.batch=batch

    def greet(self):
        print(f"{Greeter.greeting}, I am  {self.name} from batch {self.batch}")

p = Greeter("Pavel",29)
p.greet()
