class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animals(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        self.__animals += 1

    def get_animals_count(self):
        return self.__animals

    def get_info(self, species):
        if species == "mammal":
            return f"Mammals in {self.name}: {', '.join(self.mammals)}"
        elif species == "fish":
            return f"Fishes in {self.name}: {', '.join(self.fishes)}"
        elif species == "bird":
            return f"Birds in {self.name}: {', '.join(self.birds)}"


name = input()
zoo = Zoo(name)
number = int(input())
for index in range(number):
    species, name = input().split()
    zoo.add_animals(species, name)

searched_species = input()
print(zoo.get_info(searched_species))
print(f"Total animals: {zoo.get_animals_count()}")
