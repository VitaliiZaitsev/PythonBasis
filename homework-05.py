#!/usr/bin/env python

"""Homework-05 by student Vitalii Zaitsev
"""

__author__ = "Зайцев Виталий Владимирович, Vitalii Zaitsev"
__copyright__ = "Copyright 2020"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Vitalii Zaitsev"
__email__ = "vvzaisev79@gmail.com"
__status__ = "Education"


# Урок 5. Работа с файлами

# 1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

# try:
#     file4user_input = open(r"user_input.txt", "w", encoding='utf-8')
#
#     user_input = "Любое значение для первого входа в цикл"
#     while not user_input == "":  # пока не пустая строка
#         user_input = input("Enter your data or empty string to exit")
#         if user_input != "":
#             file4user_input.write(user_input + "\n")
#
# finally:
#     file4user_input.close()


# --------------------------------------------------------------------------------------------------------------------
# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

# # Решил сделать с менеджером контекста (элегантнее) и со словарём
# i = 0
# file_data_dictionary = {}
# with open("user_input.txt", encoding = 'utf-8') as file4user_input:
#     for line in file4user_input:
#         i += 1
#         file_data_dictionary[i] = len(line.split())
#
# print(f"Общее количество строк в прочитанном файле: {len(file_data_dictionary)}")
# print(f"Количество слов в каждой строке: {file_data_dictionary}")


# --------------------------------------------------------------------------------------------------------------------
# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

# # Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# # Ограничения предложенного решения:
# # * Используем контрольный файл text_3.txt
# # * Предполагаем предустановленную структуру строки <Фамилия>+<Пробел>+<Зарплата>
# # * НЕ делаем проверки на ошибки конвертации и отсутствующих данных
# # * НЕ обрабатываем ситуацию дублирования фамилий
# # * Все данные из файла затаскиваем в словарь, предполагаем фамилию уникальным ключом
# employee_data_dictionary = {}
# with open("text_3.txt", encoding = 'utf-8') as employee_salaries_file:
#      for line in employee_salaries_file:
#          employee_data = line.split()
#          employee_data_dictionary[str(employee_data[0])] = float(employee_data[1])
#
# # Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# # Выполнить подсчет средней величины дохода сотрудников.
# # Ограничения предложенного решения:
# # * Используем имеющийся словарь, "удаляем" ключи (сотрудников) с зарплатой >= 20 000.0
# # * "средней величины дохода сотрудников" - это всех сотрудников? или только с доходом менее 20 тыс рублей?
# # На всякий случай считаем обе цифры
# salary_limit = 20000.0
# average_salary4underpaid_employees = 0
# average_salary = 0
# overall_employee_count = len(employee_data_dictionary)
# list_of_normal_paided_employee = []
# for key in employee_data_dictionary:
#     employee_salary = employee_data_dictionary[key]
#     average_salary += employee_salary
#     if employee_data_dictionary[key] < salary_limit:
#         average_salary4underpaid_employees += employee_salary
#     else:
#         list_of_normal_paided_employee.append(key)
#
# # "Чистим" словарь от "нормально" оплаченных работников, оставляем только недоплаченных
# for item in list_of_normal_paided_employee:
#     employee_data_dictionary.pop(item)
#
# # Считаем средние
# average_salary = round(average_salary / overall_employee_count)
# average_salary4underpaid_employees = round(average_salary4underpaid_employees / len(employee_data_dictionary))
#
# # Вывод
# print(f"В компании {len(employee_data_dictionary)} работников с зарплатой менее {salary_limit} рублей")
# print(employee_data_dictionary)
# print(f"Их средняя зарплата составляет {average_salary4underpaid_employees} рублей,"
#       f"Это меньше средней зарплаты по компании {average_salary} рублей на "
#       f"{average_salary - average_salary4underpaid_employees} рублей" )


# --------------------------------------------------------------------------------------------------------------------
# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

# # И снова словарь
# EN_RUS_dictionary = {'One': 'Один',
#                      'Two': 'Два',
#                      'Three': 'Три',
#                      'Four': 'Четыре'}
#
# # Используем имеющийся text_4.txt
# # Проходим по всем считанным строкам, каждое значение проверяем на наличие в словаре, переводим в translated_text
# translated_text = []
# with open("text_4.txt", encoding = 'utf-8') as input_file:
#     words = {}
#     for line in input_file:
#         words = line.split()
#         i = 0
#         while i < len(words):
#             if EN_RUS_dictionary.get(words[i]):
#                 words[i] = EN_RUS_dictionary.get(words[i])
#             i += 1
#         translated_text.append(' '.join(words)+'\n')
#
# # Результирующий перевод записываем в новый текстовый файл
# translated_file = open("text_4_translated.txt", "w", encoding = 'utf-8')
# translated_file.writelines(translated_text)
# translated_file.close()


# --------------------------------------------------------------------------------------------------------------------
# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

# # Шаг 1. Генерим числа
# from random import randint
# my_list = [str(randint(0,300)) for i in range(13)]
#
# # Шаг 2. Записываем в файл
# output_file = open("text_5_output.txt", "w", encoding='utf-8')
# output_file.write(' '.join(my_list))
# output_file.close()
#
# # Шаг 3. Считываем файл, подсчитываем сумму чисел и выводим на экран
# numbers = []
# with open("text_5_output.txt", encoding = 'utf-8') as input_file:
#     words = []
#     for line in input_file:
#         numbers = line.split()
#
# sum = 0
# for item in numbers:
#     sum += int(item)
#
# print(f"Сумма чисел в файле: {sum}")


# --------------------------------------------------------------------------------------------------------------------
# 6. Необходимо создать (не программно) текстовый файл, где
# каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

# # Принимаем следующие ограничения:
# # * Каждый предмет - в отдельной строке, предметы НЕ повторяются
# # * Предмет имеет признак :   Всё, что левее : - название предмета
# # * Любые слитные блоки цифр в строке - это часы по предмету
#
# dictionary = {}
#
# with open("text_6.txt", encoding = 'utf-8') as input_file:
#     tokens_list = []
#     for line in input_file:
#         # Проверяем - есть ли вхождение :
#         delimeter_position = line.rfind(':')
#         if delimeter_position >= 0:
#             # Вырезаем название предмета
#             subject = line[:delimeter_position]
#
#         # Считаем сумму часов по предмету, только целочисленные значения
#         ###
#         ## !!!Этот способ работает только для случая, когда цифры отделены пробелами!!!
#         ## tokens_list = line.split()
#         ## sum = 0
#         ## for item in tokens_list:
#         ##     if item.isnumeric():
#         ##         sum += item.isnumeric()
#         ###
#
#         # Этот способ работает для случая слитного написания чисел со скобками
#         num_list = []
#         num = ''
#         for char in line:
#             if char.isdigit():
#                 num = num + char
#             else:
#                 if num != '':
#                     num_list.append(int(num))
#                     num = ''
#         if num != '':
#             num_list.append(int(num))
#
#         # И итоговая сумма
#         sum = 0
#         for item in num_list:
#             sum += item
#
#         # Добавляем Предмет и Часы
#         dictionary[subject] = sum
#
# # Печатает итоговый словарь Предметов и Часов
# print(dictionary)


# --------------------------------------------------------------------------------------------------------------------
# 7. Создать (не программно) текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл,
# вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
#
# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.


# # Словарь компаний и прибылей-убыткой, + средняя прибыль по успешным компаниям
# dictionary = {}
# words = []
# average_profit = 0
# positive_companies_count = 0
#
# with open("text_7.txt", encoding = 'utf-8') as input_file:
#     for line in input_file:
#         words = line.split()
#         profit = int(words[2]) - int(words[3])
#         dictionary[words[0]] = profit
#         if profit > 0:
#             average_profit += profit
#             positive_companies_count += 1
#
# # Словарь со средней прибылью
# profit_dictionary = {'average_profit': round(average_profit / positive_companies_count, 2)}
#
# # Формируем итоговый список из 2-х словарей для сериализации
# list = [dictionary, profit_dictionary]
#
# # Сериализуем в text_7_output.json
# import json
# with open("text_7_output.json", "w", encoding='utf-8') as json_output_file:
#     json.dump(list, json_output_file, indent= 4, ensure_ascii=False, separators=(',', ': '))
