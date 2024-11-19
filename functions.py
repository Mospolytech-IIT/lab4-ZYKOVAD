# 1. Минимум 2 разные функции, которые принимают на вход один или несколько параметров.
# Функции ДОЛЖНЫ выбрасывать исключение при определённых значениях входных параметров.
# Функции НЕ ДОЛЖНЫ содержать никаких обработчиков исключений.
import math


def mult(num1, num2):
    return num1*num2


def fact(num):
    factorial = 1
    while num > 1:
        factorial = factorial * num
        num = num - 1
    return factorial

# 2. Функция, которая принимает на вход один или несколько параметров.
# Функция ДОЛЖНА выбрасывать исключение при определённых значениях входных параметров.
# Функция ДОЛЖНА содержать ОДИН обработчик исключений общего типа (Exception).
# Внутри блока обработки исключения ДОЛЖНА быть какая-нибудь логика, связанная с обработкой исключения.
# Обработчик НЕ ДОЛЖЕН содержать блок finally.


def fact_except(num):
    try:
        factorial = 1
        while num > 1:
            factorial = factorial * num
            num = num - 1
        return factorial
    except:
        return "Введены некорректные данные."

# 3. Функция, которая принимает на вход один или несколько параметров.
# Функция ДОЛЖНА выбрасывать исключение при определённых значениях входных параметров.
# Функция ДОЛЖНА содержать ОДИН обработчик исключений общего типа (Exception).
# Внутри блока обработки исключения ДОЛЖНА быть какая-нибудь логика, связанная с обработкой исключения.
# Обработчик ДОЛЖЕН содержать блок finally. Логика внутри блока finally ДОЛЖНА способствовать нормальному завершению работы функции.


def fact_except_finally(num):
    try:
        factorial = 1
        while num > 1:
            factorial = factorial * num
            num = num - 1
        print(factorial)
    except:
        print("Введены некорректные данные.")
    finally:
        print("Выполнение функции завершено.")

# 4. Минимум 3 разные функции, которые принимают на вход один или несколько параметров.
# Функции ДОЛЖНЫ выбрасывать исключения при определённых значениях входных параметров.
# Функции ДОЛЖНЫ содержать НЕСКОЛЬКО обработчиков РАЗНЫХ типов исключений (минимум 3 типа исключений).
# Внутри блоков обработки исключения ДОЛЖНА быть какая-нибудь логика, связанная с обработкой
# соответствующего типа исключения. Каждый обработчик МОЖЕТ содержать блок finally. Логика внутри блока finally ДОЛЖНА способствовать нормальному завершению работы функции.


def get_by_id(id):
    names = ["Masha", "Misha", "Dasha", "Pasha"]
    try:
        return names[id]
    except IndexError:
        return "Такого элемента не существует"
    except TypeError:
        return "id введен некорректно"


def get_age_by_name(name):
    ages = {"Masha": 18, "Misha": 20, "Dasha": 20, "Pasha": 22}
    try:
        return ages[name]
    except KeyError:
        return "Такого пользователя в системе нет"


def exp(number):
    try:
        return math.exp(number)
    except OverflowError:
        return math.inf

# 5. Функция, которая принимает на вход один или несколько параметров.
# Функция ДОЛЖНА генерировать исключения при определённых условиях (в Python есть конструкция для генерации исключений).
# Функция ДОЛЖНА содержать обработчики всех исключений, которые генерируются внутри этой функции.
# Внутри блоков обработки исключения ДОЛЖНА быть какая-нибудь логика, связанная с обработкой соответствующего типа исключения.
# Обработчик МОЖЕТ содержать блок finally. Логика внутри блока finally ДОЛЖНА способствовать нормальному завершению работы функции.


def create_caple(fruit, color):
    fruits = ["apple", "orange", "banana", "pear"]
    colors = ["yellow", "red", "orange"]
    try:
        if fruit not in fruits:
            raise Exception("Такого фрукта в списке нет")
        if color not in colors:
            raise Exception("Такого цвета в списке нет")
        return fruit + " has " + color + " color"
    except Exception as e:
        return e

# 6. Минимум 3 разных пользовательских исключения и примеры их использования
# пример 1


class NameException(Exception):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Недопустимое значение: {self.name}. " \
               "Имя должно начинаться с заглавной буквы."


def set_name(name):
    try:
        if name[0].isupper():
            print(name)
        else:
            raise NameException(name)
    except NameException as e:
        print(e)


# пример 2
class AgeException(Exception):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"Недопустимое значение: {self.age}. " \
               "Возраст должен быть в диапазоне от 18 до 110"


def set_age(age):
    try:
        if 17 < age < 111:
            print(age)
        else:
            raise AgeException(age)
    except AgeException as e:
        print(e)


# пример 3
class CompanyException(Exception):

    def __init__(self, company):
        self.company = company

    def __str__(self):
        return f"Недопустимое значение: {self.company}. " \
               "Такой компании не существует"


def set_company(company):
    companies = ["Google", "Yandex", "Ozon"]
    try:
        if company in companies:
            print(company)
        else:
            raise CompanyException(company)
    except CompanyException as e:
        print(e)

# 7. Функция, которая принимает на вход один или несколько параметров.
# Функция ДОЛЖНА выбрасывать пользовательское исключение, созданное на шаге 6. при определённых значениях входных параметров.
# Функция ДОЛЖНА содержать МИНИМУМ ОДИН обработчик исключений. Внутри блока обработки исключения ДОЛЖНА быть какая-нибудь логика,
# связанная с обработкой исключения. Обработчик МОЖЕТ содержать блок finally.


def create_person(name):
    try:
        if name[0].isupper():
            print(f"Пользователь с именем {name} создан")
        else:
            raise NameException(name)
    except NameException as e:
        print(e)

# 8. Минимум 3 функции, демонстрирующие работу исключений. Алгоритм функций необходимо придумать самостоятельно


# 1
def is_even(number):
    try:
        if number % 2 == 0:
            print(f"Число {number} четное.")
        else:
            raise ValueError("Число нечётное")
    except ValueError as e:
        print(e)


# 2
def divide(number1, number2):
    try:
        result = number1 / number2
        print("Результат деления: ", result)
    except ZeroDivisionError:
        print("Деление на ноль!")


# 3
def find_element(lst, element):
    try:
        if element in lst:
            print(f"Элемент {element} найден")
        else:
            raise ValueError("Элемент не найден")
    except ValueError as e:
        print(e)
