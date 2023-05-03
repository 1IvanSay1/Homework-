from pprint import pprint
with open(r"D:\IT\Проекты\Домашки\recipes.txt", 'r', encoding = "utf-8") as file:
    cook_book = {}
    for line in file:
        name_recipes = line.strip()
        ingredients_count = int(file.readline())
        ingredients = []
        for i in range(ingredients_count):
            ing = file.readline()
            ingredient_name, quantity, measure = ing.strip().split(' | ')
            recipes = {
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            }
            ingredients.append(recipes)
        file.readline()
        cook_book[name_recipes] = ingredients
    pprint(cook_book, sort_dicts=False)
# Вопрос: В итоговом ответе почемуто после 'олета' в словаре обекты ведут себя как будто использована \n, ошибку так и не нашел.