#!/usr/bin/env python

"""Homework-06 by student Vitalii Zaitsev
"""

__author__ = "Зайцев Виталий Владимирович, Vitalii Zaitsev"
__copyright__ = "Copyright 2020"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Vitalii Zaitsev"
__email__ = "vvzaisev79@gmail.com"
__status__ = "Education"


# Урок 6. Объектно-ориентированное программирование
# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, # второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.


# class TrafficLight:
#     # атрибуты класса
#     # множество допустимые цвета
#     __color = {"Red", "Yellow", "Green"}
#     # множество включён/выключен
#     __status = {"TurnedON", "TurnedOFF"}
#
#     # методы класса
#     # вывод красным цветом
#     def __out_red(self, text):
#         print("\033[31m {}".format(text))
#
#     # вывод жёлтым цветом
#     def __out_yellow(self, text):
#         print("\033[33m {}".format(text))
#
#     # вывод зелёным цветом
#     def __out_green(self, text):
#         print("\033[32m {}".format(text))
#
#     # вывод чёрным цветом
#     def __out_black(self, text):
#         print("\033[30m {}".format(text))
#
#     # 1 цикл работы светофора, длительности заданы прямо в коде
#     def running(self):
#         import time
#
#         self.__status = "TurnedON"
#         self.__out_black("Светофор работает в автоматическом режиме")
#         # работаем в автоматическом режиме:
#         # красный цвет: 7 секунд,
#         # желтый цвет: 2 секунды,
#         # зеленый цвет: 7 секунд
#         # желтый цвет: 2 секунды,
#
#         # красный цвет
#         self.__color = "Red"
#         self.__out_red('Включён красный режим светофора, время работы: 7 секунд')
#         time.sleep(7)
#
#         # жёлтый
#         self.__color = "Yellow"
#         self.__out_yellow('Включён жёлтый режим светофора, время работы: 2 секунды')
#         time.sleep(2)
#
#         # зелёный
#         self.__color = "Green"
#         self.__out_green('Включён зелёный режим светофора, время работы: 7 секунд')
#         time.sleep(7)
#
#         # жёлтый
#         self.__color = "Yellow"
#         self.__out_yellow('Включён жёлтый режим светофора, время работы: 2 секунды')
#         time.sleep(2)
#
#         self.__out_black('')
#
#     # остановка светофора
#     def stop(self):
#         self.__status = "TurnedOFF"
#         print("Светофор остановлен")
#
#
# MyTrafficLight = TrafficLight()
#
# user_input = 'Yes'
# while user_input == 'Yes':
#     user_input = str(input(r"Введите 'Yes' для старта-продолжения работы светофора"
#                            r" либо любой другой символ для остановки работы и выхода: "))
#     if user_input == 'Yes':
#         MyTrafficLight.running()
#
# MyTrafficLight.stop()


# -------------------------------------------------------------------------------------------------------------------
# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина *
#                       * ширина *
#                       * масса асфальта для покрытия # одного кв метра дороги асфальтом, толщиной в 1 см *
#                       * число см толщины полотна.
# Проверить работу метода.
# Например: 20м * 5000м * 25кг/см * 5см = 12500 т

# class Road:
#     # атрибуты класса
#
#     # методы класса
#     # конструктор
#     def __init__(self, width, length):
#         # ширина дорожного полотна, метр
#         self._width = width
#         # длина дорожного полотна, метр
#         self._length = length
#         # масса асфальта на 1 см, кг/сантиметры
#         self.__weight = 25
#         # типовая толщина асфальтного полотна, сантиметры
#         self.__height = 5
#
#     # расчёт требуемой массы асфальты
#     def calculate(self):
#         print(f"Требуемая масса асфальта для постройки дороги "
#               f"шириной {self._width} метров и длиной {self._length} метров "
#               f"составляет {round((self._length * self._width * self.__weight * self.__height)/1000)} тонн.")
#
#
# MyRoad = Road(20, 5000)
# MyRoad.calculate()


# -------------------------------------------------------------------------------------------------------------------
# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, # передать данные, проверить значения атрибутов, вызвать методы экземпляров).
# class Worker:
#     # атрибуты класса
#
#     # методы класса
#     # конструктор
#     def __init__(self, name, surname, position):
#         # имя
#         self.name = name
#         # фамилия
#         self.surname = surname
#         # позиция
#         self.position = position
#         # доход
#         self._income = {"wage": 5000, "bonus": 1000}
#
#     def _income_calculation(self):
#         return self._income["wage"] + self._income["bonus"]
#
#
# # Класс Position (должность) на базе класса Worker
# class Position(Worker):
#     # Методы класса
#     def get_full_name(self):
#         print(f"Полное имя: {self.name}  {self.surname}.")
#
#     def get_total_income(self):
#         print(f"Доход: {self._income_calculation()} рублей.")
#
#
# MyPosition = Position("Виталий", "Зайцев", "Python-разработчик")
# MyPosition.get_full_name()
# MyPosition.get_total_income()


# -------------------------------------------------------------------------------------------------------------------
# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), чтобы сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
# class Car:
#     # атрибуты класса
#
#     # методы класса
#     # конструктор
#     def __init__(self, speed, name, color):
#         self._type = 'Общий класс авто'
#         self._is_police = False
#         self.name = name
#         self.color = color
#
#         if speed > 0:
#             self._speed = speed
#             self._turnedON = True
#             self._direction = 'вперёд'
#             self.go()
#         else:
#             self._speed = 0
#             self._turnedON = False
#             self._direction = ''
#
#     # завести машину, но никуда не ехать ()
#     def go(self):
#         # чуть-чуть сэмулируем реальную логику автомобиля - если авто уже едет, то "включить" его снова нельзя
#         # иначе "включаем"
#         if not self._turnedON:
#             self._turnedON = True
#             self._speed = 0
#         print(f"Машинка {self.name} цвет {self.color}: завелись")
#
#     def stop(self):
#         if self._turnedON:
#             self._turnedON = False
#             self._speed = 0
#         print(f"Машинка {self.name} цвет {self.color}: остановились и выключились")
#
#     def turn(self, direction):
#
#         if not self._turnedON:
#             print("Сначала заведите машину")
#         else:
#             if direction == 'вперёд':
#                 self._direction = direction
#                 self._speed += 10
#                 print(f"Едем {self._direction} со скоростью {self._speed} км/ч")
#             elif direction == 'назад':
#                 self._direction = direction
#                 self._speed -= 10
#                 if self._speed > 0:
#                     print(f"Сбавляем скорость до {self._speed} км/ч")
#                 else:
#                     self.stop()
#             elif direction == 'налево':
#                 self._direction = direction
#                 print(f"Едем {self._direction} со скоростью {self._speed} км/ч")
#             elif direction == 'направо':
#                 self._direction = direction
#                 print(f"Едем {self._direction} со скоростью {self._speed} км/ч")
#             else:
#                 print(f"Недопустимое значение направления."
#                       f"продолжаем двигаться {self._direction} "
#                       f"со скоростью {self._speed} км/ч")
#
#     def show_speed(self):
#         print(f"Скорость автомобиля: {self._speed} км/ч")
#
#
# # Городской автомобиль
# class TownCar(Car):
#     # методы класса
#     # конструктор
#     def __init__(self, speed, name, color):
#         super().__init__(speed, name, color)
#         self._type = 'Городской автомобиль'
#         self.color = color
#         self.name = name
#         self.is_police = False
#         self._speed_limit = 60
#
#         if speed > 0:
#             self._speed = speed
#             self.check_speed()
#             self._turnedON = True
#             self._direction = 'вперёд'
#             self.go()
#         else:
#             self._speed = 0
#             self._turnedON = False
#             self._direction = ''
#
#     # Проверка скорости
#     def check_speed(self):
#         if self._speed > self._speed_limit:
#             print(f"Вы двигаетесь с превышением скорости: ваша скорость {self._speed} км/ч, "
#                   f"ограничение: {self._speed_limit} км/ч")
#
#
# # Спортивный автомобиль
# class SportCar(Car):
#     # методы класса
#     # конструктор
#     def __init__(self, speed, name, color):
#         super().__init__(speed, name, color)
#         self._type = 'Спортивный автомобиль'
#         self.color = color
#         self.name = name
#         self.is_police = False
#
#         if speed > 0:
#             self._speed = speed
#             self._turnedON = True
#             self._direction = 'вперёд'
#             self.go()
#         else:
#             self._speed = 0
#             self._turnedON = False
#             self._direction = ''
#
#
# # Автомобиль хозяйственных служб
# class WorkCar(Car):
#     # методы класса
#     # конструктор
#     def __init__(self, speed, name, color):
#         super().__init__(speed, name, color)
#         self._type = 'Автомобиль хозяйственных служб'
#         self.color = color
#         self.name = name
#         self.is_police = False
#         self._speed_limit = 40
#
#         if speed > 0:
#             self._speed = speed
#             self.check_speed()
#             self._turnedON = True
#             self._direction = 'вперёд'
#             self.go()
#         else:
#             self._speed = 0
#             self._turnedON = False
#             self._direction = ''
#
#     # Проверка скорости
#     def check_speed(self):
#         if self._speed > self._speed_limit:
#             print(f"Вы двигаетесь с превышением скорости: ваша скорость {self._speed} км/ч, "
#                   f"ограничение: {self._speed_limit} км/ч.")
#
#
# # Полицейский автомобиль
# class PoliceCar(Car):
#     # методы класса
#     # конструктор
#     def __init__(self, speed, name, color):
#         super().__init__(speed, name, color)
#         self._type = 'Полицейский автомобиль'
#         self.color = color
#         self.name = name
#         self.is_police = True
#
#         if speed > 0:
#             self._speed = speed
#             self._turnedON = True
#             self._direction = 'вперёд'
#             self.go()
#         else:
#             self._speed = 0
#             self._turnedON = False
#             self._direction = ''
#
#
# # Создайте экземпляры классов, передайте значения атрибутов.
# # Выполните доступ к атрибутам, выведите результат.
# # Выполните вызов методов и также покажите результат.
#
# myTownCar = TownCar(0, "Миниавтомобильчик", "Красненький")
# mySportCar = SportCar(100, "Зум-Зум", "Тоже красненький")
# myWorkCar = WorkCar(0, "Грузовик", "Белый")
# myPoliceCar = PoliceCar(10, "Полиция", "Синий")
#
# # История грузовика
# # завелись
# myWorkCar.go()
# # набрали 40
# myWorkCar.turn("вперёд")
# myWorkCar.turn("вперёд")
# myWorkCar.turn("вперёд")
# myWorkCar.turn("вперёд")
# # проверили скорость
# myWorkCar.check_speed()
# # повернули налево
# myWorkCar.turn("налево")
# # остановились
# myWorkCar.stop()
#
#
# # История минимашинки
# # сначала неудачно поворачиваем налево
# myTownCar.turn("налево")
# # поняли, что надо завестись - заводимся
# myTownCar.go()
# # давим тапку, не смотрим на скорость
# myTownCar.turn("вперёд")
# myTownCar.turn("вперёд")
# myTownCar.turn("вперёд")
# myTownCar.turn("вперёд")
# myTownCar.turn("вперёд")
# myTownCar.turn("вперёд")
# myTownCar.turn("вперёд")
# # ловим ораничение скорости
# myTownCar.check_speed()
# # уменьшаем скорость
# myTownCar.turn("назад")
# # показываем нашу скорость
# myTownCar.show_speed()
# # поворачиваем налево и налево (поворот на 180 градусов)
# myTownCar.turn("налево")
# # останавливаемся
# myTownCar.stop()
#
# # История спортивной машины
# # играем в шашечки и останавливаемся в пункте назначения
# mySportCar.show_speed()
# mySportCar.turn("налево")
# mySportCar.turn("вперёд")
# mySportCar.turn("направо")
# mySportCar.turn("вперёд")
# mySportCar.turn("налево")
# mySportCar.turn("вперёд")
# mySportCar.turn("направо")
# mySportCar.turn("вперёд")
# mySportCar.show_speed()
# mySportCar.stop()
#
# # История полицейской машины
# # просто едем
# myPoliceCar.turn("вперёд")
# myPoliceCar.turn("вперёд")
# myPoliceCar.turn("вперёд")
# myPoliceCar.turn("вперёд")
# myPoliceCar.turn("вперёд")
# myPoliceCar.turn("вперёд")
# myPoliceCar.turn("вперёд")
# myPoliceCar.show_speed()


# -------------------------------------------------------------------------------------------------------------------
# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

# class Stationery:
#     def __init__(self, title):
#         self.title = title
#
#     def draw(self):
#         print("Общий метод: запуск отрисовки")
#
#
# class Pen(Stationery):
#     def draw(self):
#         print(f"Запуск отрисовки для {self.title}")
#
#
# class Pencil(Stationery):
#     def draw(self):
#         print(f"Запуск отрисовки для {self.title}")
#
#
# class Handle(Stationery):
#     def draw(self):
#         print(f"Запуск отрисовки для {self.title}")
#
#
# # Создаём экземпляры
# myPen = Pen("Ручка")
# myPencil = Pencil("Карандаш")
# myHandle = Handle("Маркер")
#
# # Проверяем работу метода Draw
# myPen.draw()
# myPencil.draw()
# myHandle.draw()
