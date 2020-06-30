# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула
# (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
# show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод
# show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
# вызов методов и также покажите результат.

class Car:
    # attributes
    speed = None
    color = None
    name = None
    is_police = False

    # methods
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} is driven."

    def stop(self):
        return f"{self.name} is stopped."

    def turn(self, direction):
        return f"{self.name} is turned to the " + direction + "."

    def show_speed(self):
        return f"Your current speed is {self.speed}"


# subclasses
class TownCar(Car):
    # methods
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f"Your speed is {self.speed} that is higher than allowed. Please reduce."
        else:
            return f"Your speed is {self.speed} is within the road rules."


class SportCar(Car):
    # methods
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    # methods
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f"Your speed is {self.speed} that is higher than allowed. Please reduce."
        else:
            return f"Your speed is {self.speed} is within the road rules."


class PoliceCar(Car):
    # methods
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


bmw = SportCar(100, "Red", "BMW", False)
toyota = TownCar(30, "White", "Toyota", False)
nissan = WorkCar(70, "Blue", "Nissan", False)
ford = PoliceCar(110, "Black",  "Ford", True)

print(bmw.turn("left"))
print(f'First {toyota.turn("right")} But then {toyota.stop()}')
print(f'{bmw.go()} {bmw.show_speed()}')
print(f'{nissan.name} is {nissan.color}.')
print(toyota.show_speed())
print(nissan.show_speed())
print(ford.show_speed())