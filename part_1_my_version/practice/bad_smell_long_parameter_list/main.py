# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, field, default_speed: float = 1.0):
        self.field = field
        self.speed: float = default_speed
        self.state: str = ''

    def move(self, direction: str, x_coord: float, y_coord: float, state: str):
        match state:
            case 'fly':
                self.speed *= 1.2
            case 'crawl':
                self.speed *= 0.5
        self._move(direction, x_coord, y_coord, self.speed)

    def _move(self, direction, x_coord, y_coord, speed):
        match direction:
            case 'UP':
                self.field.set_unit(x=x_coord, y=y_coord + speed, unit=self)
            case 'DOWN':
                self.field.set_unit(x=x_coord, y=y_coord - speed, unit=self)
            case 'LEFT':
                self.field.set_unit(x=x_coord - speed, y=y_coord, unit=self)
            case 'RIGTH':
                self.field.set_unit(x=x_coord + speed, y=y_coord, unit=self)
            case _:
                self.field.set_unit(x=x_coord, y=y_coord, unit=self)
