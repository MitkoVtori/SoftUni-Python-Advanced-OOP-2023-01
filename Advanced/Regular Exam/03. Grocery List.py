def shop_from_grocery_list(budget, grocery_list: list, *products):
    bought_products = []

    bought_all_products = True

    for product_price in products:
        product, price = product_price

        if budget >= price and product not in bought_products and product in grocery_list:
            budget -= price
            bought_products.append(product)

        elif budget < price:
            bought_all_products = False
            break

    if bought_all_products and not [x for x in grocery_list if x not in bought_products]:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."

    return f"You did not buy all the products. Missing products: {', '.join([product for product in [x for x in grocery_list if x not in bought_products]])}."


''' TESTS '''
# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("tomato", 20.45),
# ))
# print()
# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat"],
#     ("cola", 5.8),
#     ("tomato", 10.0),
#     ("meat", 22),
# ))
# print()
# print(shop_from_grocery_list(
#     100,
#     ["tomato", "cola", "chips", "meat", "chocolate"],
#     ("cola", 15.8),
#     ("chocolate", 30),
#     ("tomato", 15.85),
#     ("chips", 50),
#     ("meat", 22.99),
# ))