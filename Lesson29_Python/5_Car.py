class Car:
    def __init__(self, make, model, color, year):
        self.make = make
        self.model = model
        self.color = color
        self.year = year

    def get_make(self):
        return self.make

    def set_make(self, new_make):
        self.make = new_make

    def get_model(self):
        return self.model

    def set_model(self, new_model):
        self.model = new_model

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        self.color = new_color

    def get_year(self):
        return self.year

    def set_year(self, new_year):
        self.year = new_year

# Создаем объекты класса Car
car1 = Car("Toyota", "Camry", "silver", 2022)
car2 = Car("Ford", "Mustang", "red", 2021)
car3 = Car("Honda", "Civic", "black", 2020)

# Вызываем методы для каждого объекта
print(f"Car 1: Make - {car1.get_make()}, Model - {car1.get_model()}, Color - {car1.get_color()}, Year of manufacture - {car1.get_year()}")
car1.set_color("белый")
print(f"Updated car color 1: {car1.get_color()}")

print(f"Car 2: Make - {car2.get_make()}, Model - {car2.get_model()}, Color - {car2.get_color()}, Year of manufacture - {car2.get_year()}")
car2.set_year(2023)
print(f"Updated vehicle year 2: {car2.get_year()}")

print(f"Car 3: Make - {car3.get_make()}, Model - {car3.get_model()}, Color - {car3.get_color()}, Year of manufacture - {car3.get_year()}")
car3.set_model("Accord")
print(f"Updated car model 3: {car3.get_model()}")
