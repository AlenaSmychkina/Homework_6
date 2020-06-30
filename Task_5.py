# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
# (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
# выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
# экземпляра.


class Stationery:
    # attributes
    title = "Title"

    # method
    def draw(self):
        print(f"Start drawing with a {self.title}.")


# subclasses
class Pen(Stationery):
    # attributes
    title = "pen"

    # method
    def draw(self):
        super(Pen, self).draw()
        print("Drawing with a pen.")


class Pencil(Stationery):
    # attributes
    title = "pencil"

    # method
    def draw(self):
        super(Pencil, self).draw()
        print("Drawing with a pencil.")


class Handle(Stationery):
    # attributes
    title = "handle"

    # method
    def draw(self):
        super(Handle, self).draw()
        print("Drawing with a handle.")


my_pen = Pen()
my_pencil = Pencil()
my_handle = Handle()

my_pen.draw()
my_pencil.draw()
my_handle.draw()

