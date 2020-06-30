# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
# массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса
# асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна. Проверить работу
# метода. Например: 20м * 5000м * 25кг * 5см = 12500 т""


class Road:
    # attributes
    _length = None
    _width = None
    weight = None
    thickness = None

    # methods
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def intake(self):
        self.weight = 0.025
        self.thickness = 0.05
        intake = self._length * self._width * self.weight * self.thickness
        return intake


l = float(input("Enter the road length: "))
w = float(input("Enter the road width: "))
a = Road(l, w)

print(f"You need {a.intake()} ton of asphalt to build this road.")