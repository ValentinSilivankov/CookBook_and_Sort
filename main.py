import os
from pprint import pprint

def get_cook_book():
    with open('recipes.txt', encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            dish_name = line.strip()
            ingredients_count = int(file.readline())
            ingredients = []
            for ing in range(ingredients_count):
                ingredient = file.readline().strip()
                name, quan, meas = ingredient.split(' | ')
                ingredients.append({
                    'ingredient_name': name,
                    'quantity': quan,
                    'measure': meas
                })
            file.readline()
            cook_book[dish_name] = ingredients
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingr in get_cook_book()[dish]:
            if ingr['ingredient_name'] in shop_list.keys():
                shop_list[ingr['ingredient_name']]['quantity'] = \
                    int(shop_list[ingr['ingredient_name']]['quantity']) + int(ingr['quantity']) * person_count
            else:
                shop_list[ingr['ingredient_name']] = {
                    'measure': ingr['measure'],
                    'quantity': int(ingr['quantity']) * person_count
                }
    pprint(shop_list)   


get_shop_list_by_dishes(['Фахитос', 'Омлет'], 5)


def file_sort():
    list_files = []
    for files in os.listdir(os.path.join(os.getcwd(), 'sorting')):
        list_files.append(files)
    a = {}
    for file in list_files:
        with open(os.path.join(os.getcwd(), 'sorting', file), 'r', encoding='utf-8') as f:
            count = 0
            b =[]
            for line in f:
                count += 1
                b.append(line)
                a[file] = [count, b]
    with open('sorted_file.txt', 'w'):
        pass
    while a != {}:
        for name_file, len in a.items():
            min_text = min(a.values())
            if len == min_text:
                text = len[1][0:]
                with open('sorted_file.txt', 'a', encoding='utf-8') as d:
                    d.write(f'{name_file} 1 \n{len[0]} 2 \n')
                    d.writelines(text)
                    d.write(' 3 \n')
                    del a[name_file]
                    break


file_sort()