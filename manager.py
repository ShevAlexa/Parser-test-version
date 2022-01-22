import json
import os


def add_product(dish: str, composition: str, weight: int, price: float, quantity: int):
    if os.path.getsize('dish.json') > 0:
        with open('dish.json', 'r', encoding='utf-8') as dish_file:
            dish_dict = json.load(dish_file)
    else:
        print("First dish, it's cool!")

    new_dish = list()
    new_dish.append(dish)
    new_dish.append(composition)
    new_dish.append(weight)
    new_dish.append(price)
    new_dish.append(quantity)

    new_dish = dict(zip(header, new_dish))
    print(new_dish, '\n')

    try:
        dish_dict[new_dish['Dish']] = new_dish
    except NameError:
        dish_dict = dict()
        dish_dict[new_dish['Dish']] = new_dish

    with open('dish.json', 'w', encoding='utf-8') as dish_file:
        json.dump(dish_dict, dish_file, indent=5)

    return 0


def delete_product(name):
    if os.path.getsize('dish.json') > 0:
        with open('dish.json', 'r', encoding='utf-8') as dish_file:
            dish_dict = json.load(dish_file)
    else:
        print(msg, '(File is empty)\n')
        return "Mistake"

    if name in dish_dict:
        print(f'{dish_dict[name]} - deleted\n')
        del dish_dict[name]
    else:
        print('No such dish in menu\n')

    with open('dish.json', 'w', encoding='utf-8') as dish_file:
        json.dump(dish_dict, dish_file, indent=5)

    return 0


def search_product(name):
    if os.path.getsize('dish.json') > 0:
        with open('dish.json', 'r', encoding='utf-8') as dish_file:
            dish_dict = json.load(dish_file)
    else:
        print(msg, '(File is empty)\n')
        return "Mistake"

    dish_counter = 0
    for item in dish_dict:
        if name.lower() in item.lower():
            dish_counter += 1
            print(dish_dict[item])
    if dish_counter == 0:
        print('No such dish in menu\n')

    return 0


def edit_product(name):
    if os.path.getsize('dish.json') > 0:
        with open('dish.json', 'r', encoding='utf-8') as dish_file:
            dish_dict = json.load(dish_file)
    else:
        print(msg, '(File is empty)\n')
        return "Mistake"

    if name not in dish_dict:
        print(msg, '(No such dish in menu)\n')
        return "Mistake"

    else:
        print(dish_dict[name])
        while True:
            position = input('enter position in dish u want to edit: ')
            if position not in dish_dict[name]:
                print(msg, '(No such position in menu)\n')
                continue
            else:
                print(f'Old information: {dish_dict[name][position]}')
                new_information = input('enter new information: ')
                dish_dict[name][position] = new_information
                print('Сhanges were successful\n')
                break

    with open('dish.json', 'w', encoding='utf-8') as dish_file:
        json.dump(dish_dict, dish_file, indent=5)

    return 0

# тело программы

header = ['Dish', 'Composition', 'Weight', 'Price', 'Quantity']
msg = 'Any mistake, try again, please'

while True:
    action = input('what u want to do: ')

# проверка наличия основного и резервного файлов в директории

    try:
        os.path.getsize('dish.json')
    except IOError as error:
        file = open('dish.json', 'x', encoding='utf-8')
        file.close()
        print('New file\n')

    try:
        os.path.getsize('dish_copy.json')
    except IOError:
        file = open('dish_copy.json', 'x', encoding='utf-8')
        file.close()
        print('New reserve file\n')

# резервное копирование файла

    if os.path.getsize('dish.json') > 0:
        with open('dish.json', 'r', encoding='utf-8') as dish_file:
            dish_dict = json.load(dish_file)
        with open('dish_copy.json', 'w', encoding='utf-8') as dish_file_copy:
            json.dump(dish_dict, dish_file_copy, indent=5)
    else:
        if os.path.getsize('dish_copy.json') > 0:
            with open('dish_copy.json', 'r', encoding='utf-8') as dish_file_copy:
                dish_dict = json.load(dish_file_copy)
            with open('dish.json', 'w', encoding='utf-8') as dish_file:
                json.dump(dish_dict, dish_file, indent=5)

# обработка запросов

    # добавить новое блюдо

    if action.lower() in 'add':
        dish = input('dish name is: ')
        composition = input('composition is (separately): ')
        weight = int(input('weight is: '))
        price = float(input('price is: '))
        quantity = int(input('quantity is: '))

        add_product(dish, composition, weight, price, quantity)

    # удалить блюдо из меню

    elif action.lower() in 'delete':
        name = input('enter the dish u want to delete: ')
        delete_product(name)

    # найти блюдо в меню

    elif action in 'search':
        name = input('enter the name to search: ')
        search_product(name)

    # изменить блюдо

    elif action == 'edit':
        name = input('enter the dish u want to edit: ')
        edit_product(name)

    # выход из скрипта

    elif action == 'exit':
        exit()

# обработка ошибки отсутствия запрашиваемого действия

    else:
        print(msg, '(No such function)')
        continue
