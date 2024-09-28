class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        floor = 0
        print(f'I call the elevator to the {new_floor} floor')
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Such a floor does not exist')
        else:
            for floor in range(new_floor):
                print(floor + 1)

    def __len__(self):
        return self.number_of_floors


    def __str__(self):
        return f'Name: {self.name}, number of floors: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors


    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors


    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors


    def __add__(self, other):
        return self

    def __radd__(self, other):
        return self

    def __iadd__(self, other):
        return self

h1 = House('Хрущевка', 5)
h2 = House('Москва сити', 76)
h1.go_to(4)
h2.go_to(80)
print(h1)
print(h2)
print(len(h1))
print(len(h2))
print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
