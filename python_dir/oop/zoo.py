#!python3

class Cat:
    def __init__(self, name):
        self.name = name
        self.coat = 'striped'
        self.size = 200
        self.diet = 'meat'
        self.health = 500
        self.happiness = 300

    def eat(self, amount=50):
        self.health += 10
        self.size += amount/100
        return self

    def run(self):
        self.health -= 10
        self.happiness += 5
        self.size -= 5
        return self

    def laz(self):
        self.health -= 5
        self.happiness -=15
        return self

    def display_info(self):
        print("="*30)
        print("Name: ", self.name)
        print("Coat: ", self.coat)
        print("size: ", self.size)
        print("Health: ", self.health)
        print("happiness: ", self.happiness)


class Lion(Cat):
    def __init__(self, name):
        super().__init__(name)
        self.coat = "gold"


class Tiger(Cat):
    def __init__(self, name):
        super().__init__(name)
        self.coat = 'striped'


class Hippo:
    def __init__(self, name):
        self.name = name
        self.weight = 5000
        self.temperment = "angry"

    def display_info(self):
        print("="*30)
        print("Name: ", self.name)
        print("Weight: ", self.weight)
        print("temperment: ", self.temperment)


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_lion(self, name):
        self.animals.append( Lion(name) )

    def add_hippo(self, name):
        self.animals.append( Hippo(name) )

    def add_tiger(self, name):
        self.animals.append( Tiger(name) )

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

def main():
    zoo1 = Zoo("John's Zoo")
    zoo1.add_lion("Nala")
    zoo1.add_hippo("Berry")
    zoo1.add_lion("Simba")
    zoo1.add_tiger("Rajah")
    zoo1.add_tiger("Shere Khan")
    zoo1.print_all_info()

if __name__ == '__main__':
    main()
