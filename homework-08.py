#!/usr/bin/env python

"""Homework-08 by student Vitalii Zaitsev
"""

__author__ = "Зайцев Виталий Владимирович, Vitalii Zaitsev"
__copyright__ = "Copyright 2020"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Vitalii Zaitsev"
__email__ = "vvzaisev79@gmail.com"
__status__ = "Education"

# Урок 8. ООП. Полезные дополнения

# --------------------------------------------------------------------------------------------------------------
# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

# Эта задача понята с трудом.
# Для решения пришлось просить помощи у интернета, использовал этот ресурс, FYI
# https://coderoad.ru/12179271/%D0%97%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D0%B5-classmethod-%D0%B8-staticmethod-%D0%B4%D0%BB%D1%8F-%D0%BD%D0%B0%D1%87%D0%B8%D0%BD%D0%B0%D1%8E%D1%89%D0%B8%D1%85
# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         day, month, year = map(int, date_as_string.split('-'))
#         return (0 < day <= 31) and (0 < month <= 12) and (0 < year <= 9999)
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split('-'))
#         date1 = cls(day, month, year)
#         return date1
#
#
# date2 = Date.from_string('25-09-2012')
# is_date = Date.is_date_valid('25-09-2012')
# print("Работа завершена")


# --------------------------------------------------------------------------------------------------------------
# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

# Чистый копипаст из методички к 8-му уроку. Специально подумал, надо ли добавлять что-то ещё?
# class SpecialException(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
#
# input_data = input("Введите знаменатель (знаменатель НЕ должен быть равен 0): ")
#
# try:
#     input_data = float(input_data)
#     if input_data == 0:
#         raise SpecialException("Вы ввели 0, делить на 0 нельзя")
# except ValueError:
#     print("Вы ввели не число")
# except SpecialException as err:
#     print(err)
# else:
#     print(f"Всё хорошо. Ваш знаменатель: {input_data}")


# --------------------------------------------------------------------------------------------------------------
# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована.
# Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта,
# введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.

# class OnlyNumbersAreAllowed(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
#
# # Список введённых пользователем значений, исходно пустой
# input_list = []
#
# input_stopped = False
# while not input_stopped:
#     user_input = input("Введите число или слово stop для завершения ввода: ")
#     if user_input == 'stop':
#         input_stopped = True
#         break
#     try:
#         # Не следует бояться писать понятно :)
#         # Чекаем - если нет цифр, то точно ситуация неблагополучна, генерим собственное исключение
#         if not (user_input.find('0') or user_input.find('1') or user_input.find('2') or
#                 user_input.find('3') or user_input.find('4') or user_input.find('5') or
#                 user_input.find('6') or user_input.find('7') or user_input.find('8') or
#                 user_input.find('9')):
#             raise OnlyNumbersAreAllowed("Ваш ввод НЕ содержит цифр, "
#                                         "введённое вами значение не может быть конвертировано в число. "
#                                         "Повторите ввод")
#
#         # Приводим в вещественному числу
#         user_input = float(user_input)
#
#     except ValueError:
#         print("Вы ввели не число")
#     except OnlyNumbersAreAllowed as err:
#         print(err)
#
#     else:
#         input_list.append(user_input)
#
#
# print(f"Вы ввели: {input_list}")


# --------------------------------------------------------------------------------------------------------------
# 4, 5, 6
# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.


# class Warehouse:
#
#      # Простой конструктор: имя склада
#      def __init__(self, name, storage_capacity):
#          self.name = name
#          self.things = []
#          self.storage_capacity = storage_capacity
#
#      # Добавляем технику на склад, есть минимальная проверка на непревышение ёмкости склада
#      def receipt_to_the_warehouse(self, org_technics):
#           if len(self.things) < self.storage_capacity:
#                self.things.append(org_technics)
#
#      # Списываем технику со склада
#      def receipt_to_the_warehouse(self, org_technics):
#           if org_technics in self.things:
#                self.things.remove(org_technics)
#
#
# class OrgTechnics:
#      # Модель, цвет
#      def __init__(self, model, color, title, ID):
#           self.model = model
#           self.color = color
#           self.title = title
#           self.ID = ID
#
#
# class Printer(OrgTechnics):
#      # + тип печати (струйный, лазерный)
#      def __init__(self, model, color, type_of_printing):
#           super(Printer, self).__init__(model, color)
#           self.type_of_printing = type_of_printing
#
#
# class Scanner(OrgTechnics):
#      # + тип сканирования (ручной, настольный)
#      def __init__(self, model, color, type_of_scanning):
#           super(Scanner, self).__init__(model, color)
#           self.type_of_scanning = type_of_scanning
#
#
# class Xerox(OrgTechnics):
#      # + тип ксерокса (домашний, профессиональный)
#      def __init__(self, model, color, type):
#           super(Xerox, self).__init__(model, color)
#           self.type = type


# --------------------------------------------------------------------------------------------------------------
# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.
# class ComplexNumber:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return ComplexNumber(self.x + other.x, self.y + other.y)
#
#     def __str__(self):
#         return f"({self.x} + {self.y}*j)"
#
#     def __mul__(self, other):
#         # Произведением двух комплексных чисел z1=a1+b1i и z2=a2+b2i называется комплексное число z, равное
#         # z = z1 ⋅ z2 = (a1*a2 − b1 * b2) + (a1 * b2 + b1 * a2)* i
#         return ComplexNumber((self.x * other.x - self.y * other.y), (self.x * other.y + other.x * self.y))
#
#
# a1 = 1
# b1 = 1
# a2 = 2
# b2 = 2
#
# my_Complex_number_1 = ComplexNumber(a1, b1)
# my_Complex_number_2 = ComplexNumber(a2, b2)
#
# print(f"Результаты сложения и умножения комлексных чисел с помощью собственного класса {ComplexNumber.__name__}")
# print(f"{my_Complex_number_1} + {my_Complex_number_2} = {my_Complex_number_1 + my_Complex_number_2}")
# print(f"{my_Complex_number_1} * {my_Complex_number_2} = {my_Complex_number_1 * my_Complex_number_2}")
#
# print(f"Результаты сложения и умножения комлексных чисел с помощью встроенного класса {ComplexNumber.__name__}")
# number_1 = complex(a1, b1)
# print(f"{complex(a1, b1)} + {complex(a2, b2)} = {complex(a1, b1) + complex(a2, b2)}")
# print(f"{complex(a1, b1)} * {complex(a2, b2)} = {complex(a1, b1) * complex(a2, b2)}")
