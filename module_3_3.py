values_list = [True, 12, "Cтрока"]
values_dict = {"a": 10, "b": 12, "c": 24}
values_list_2 = [54.32, "Cтрока"]


def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(3)
print_params(12, [2, 15, 10])
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)



#   1.Функция с параметрами по умолчанию:Создайте функцию print_params(a = 1, b = 'строка', c = True)
#   2. Функция должна выводить эти параметры.(например сейчас это: 1, 'строка', True).
#   3. Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
#     Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])

#   1. Создайте список values_list с тремя элементами разных типов.
#   2. Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params,
#     и значениями разных типов.
#   3.Передайте values_list и values_dict в функцию print_params, используя распаковку параметров
#      (* для списка и ** для словаря).
#   4. Создайте список values_list_2 с двумя элементами разных типовvalues_list_2
#   5. Создайте список values_list_2 с двумя элементами разных типов
#        Проверьте, работает ли print_params(*values_list_2, 42)