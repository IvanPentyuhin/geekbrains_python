"""
Реализуйте базовый класс Car:
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
"""


class Car:


    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('The car went down the road')

    def stop(self):
        print('The car is stop')

    def turn_right(self):
        print('The car turned right')

    def turn_lift(self):
        print('The car turned left')

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('speeding')
        else:
            print(self.speed)

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('speeding')
        else:
            print(self.speed)

class PoliceCar(Car):
    pass


sport_car = SportCar(150, 'Красная', 'Спортивная машина', False)
town_car = TownCar(50, 'Серая', 'Городская машина', False)
work_car = WorkCar(70, 'Желтая', 'Рабочая машина', False)
police_car = PoliceCar(10, 'Синяя', 'Полицейская машина', True)


print(town_car.show_speed())
print(sport_car.show_speed())
print(work_car.show_speed())
print(police_car.show_speed())
print(sport_car.turn_lift())

