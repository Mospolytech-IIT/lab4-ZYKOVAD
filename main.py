from functions import mult, fact, fact_except, fact_except_finally, get_by_id, get_age_by_name, exp, create_caple, \
    set_age, set_name, set_company, create_person, is_even, divide, find_element


def main_func():
    print("1.1. Результат умножения:", mult(2, 3))  # исключение при вводе двух строк
    print("1.2. Факториал:", fact(3))  # исключение при вводе строки
    print("2. Факториал: ", fact_except(3))  # выполнение блока except при вводе строки
    print("3. Факториал: ")
    fact_except_finally(5)
    print("4.1. Имя:", get_by_id(2))
    print("4.2. Возраст:", get_age_by_name('Dasha'))
    print("4.3. Экспонента:", exp(10000))
    print("5.", create_caple("apple", "red"))
    print("6.1. Установить имя")
    set_name("dasha")
    print("6.2. Установить возраст")
    set_age(18)
    print("6.3. Установить место работы")
    set_company("Ozon")
    print("7. Создание пользователя")
    create_person("dasha")
    print("8.1. Проверка четности числа")
    is_even(5)
    print("8.2. Деление")
    divide(4, 0)
    print("8.3. Поиск элемента в списке")
    find_element([1, 2, 3, 4], 5)


if __name__ == "__main__":
    main_func()
