def shopping_cart(*products):
    meals = {"Soup": 3, "Pizza": 4, "Dessert": 2}
    meal_products = {"Soup": [], "Pizza": [], "Dessert": []}

    for product in products:

        if product == "Stop":
            break

        if product[0] in meals.keys():
            if meals[product[0]] > 0:
                meals[product[0]] -= 1
                if product[1] not in meal_products[product[0]]:
                    meal_products[product[0]].append(product[1])

    sorted_meals = sorted(meal_products.items(), key=lambda x: (-len(x[1]), x[0]))

    checker = 0
    for meal in sorted_meals:
        if not meal[1]:
            checker += 1

    if checker == 3:
        return "No products in the cart!"

    output = ''

    for list_products in sorted_meals:
        sorted_products = '\n'.join([f' - {product}' for product in sorted(list_products[1])])
        output += f"{list_products[0]}:\n{sorted_products}\n"

    return output # output[:-1] in case you don't want the last line.


''' TESTS '''
# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Soup', 'carrots'),
#     ('Pizza', 'cheese'),
#     ('Pizza', 'flour'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'mushrooms'),
#     ('Pizza', 'tomatoes'),
#     'Stop',
# ))
# print()
# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))
# print()
# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
# ))
