class dog:
    def __init__(self,name, dogage, hp):
        self.name = name
        self.dogage = dogage
        self.hp = hp
    def show_info(self):
        print(self.name)
        print(self.dogage)
        print(self.hp)
s = dog("Name = Sharik","age = 15", "health = 100")
s.show_info()
