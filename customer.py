import json
import os
from datetime import datetime


try:
    os.path.getsize('dish.json')
except IOError as error:
    print('File is not found')
    exit()
else:
    if os.path.getsize('dish.json') > 0:
        with open('dish.json', 'r', encoding='utf-8') as dish_file:
            dish_dict = json.load(dish_file)
    else:
        print('File is empty')
        exit()

while True:
    try:
        first_input = int(input('choose the action: (description - 1, price - 2, quantity - 3'
                                ', menu - 4, bar - 5, ): '))
    except ValueError:
        continue

    if first_input == 1:
        for key in dish_dict:
            print(key, ':', dish_dict[key]['Composition'])
    elif first_input == 2:
        for key in dish_dict:
            print(key, '-', dish_dict[key]['Price'])
    elif first_input == 3:
        for key in dish_dict:
            print(key, '-', dish_dict[key]["Weight"])
    elif first_input == 4:
        for key in dish_dict:
            print(dish_dict[key])
    elif first_input == 5:
        for key in dish_dict:
            pass

    else:
        print('Any mistake, try again')
        continue
    print('Are u ready to order?')

    second_input = input('(Yes/No) ')
    if second_input.lower() in 'yes':
        break
    else:
        continue

basket = list()
while True:
    third_input = input('what u wish? (please, enter the dishes correctly): ')
    if third_input == 'nothing':
        break
    elif third_input == 'basket':
        print(basket)
        continue
    for item in dish_dict:
        if third_input == item and dish_dict[item]["Quantity"] != 0:
            basket.append(item)
            dish_dict[item]["Quantity"] -= 1
            print('Yes, next')
            break
        elif third_input == item and dish_dict[item]["Quantity"] == 0:
            print('no more such meal')
            break
    else:
        print('No such dish')

if basket:
    print('Your ', end='')
    for item in basket:
        print(item, end=' ')
else:
    print('Have a nice day')
    exit()

count_receipt = 0
for item in basket:
    for meal in dish_dict:
        if item == meal:
            count_receipt += dish_dict[meal]['Price']
count_receipt = '%.2f' % count_receipt
print(f'\nIn total - {count_receipt}', '\nHave a nice day!\n')

with open('sales_analysis.txt', 'a', encoding='utf-8') as file:
    file.write(f'{str(count_receipt)}$ {datetime.now().date()} \n')

with open('dish.json', 'w', encoding='utf-8') as dish_file:
    json.dump(dish_dict, dish_file, indent=5)

with open('dish_copy.json', 'w', encoding='utf-8') as dish_copy_file:
    json.dump(dish_dict, dish_copy_file, indent=5)
