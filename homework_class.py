# ооп создание классов:

class Cat:
    family = 'feline'
    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color

    def run(self):
        return "I can run and meow"

    def say_hello(self):
        return f"Hello! My name is {self.name}. Meow!"

# создание подкласса. Наследование, инкапсуляция классов:

class Home_cat(Cat):
    def __init__(self, name, weight, color, age):
        super().__init__(name, weight, color)
        self.__age = age

    def food(self):
        return f"I eat cat's food"

cat_1 = Home_cat('Kitty', 3, 'grey', 2)
print(cat_1.food())
print(cat_1.__dict__)