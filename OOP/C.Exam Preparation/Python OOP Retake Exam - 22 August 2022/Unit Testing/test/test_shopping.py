from unittest import TestCase, main
from project.shopping_cart import ShoppingCart


class TestShoppingCart(TestCase):

    def setUp(self) -> None:
        self.shopping_cart = ShoppingCart("Fantastico", 16.50)

    def test_successful_initialization(self):
        self.assertEqual("Fantastico", self.shopping_cart.shop_name)
        self.assertEqual(16.50, self.shopping_cart.budget)
        self.assertEqual({}, self.shopping_cart.products)

    def test_invalid_shop_name(self):
        with self.assertRaises(ValueError) as ve:
            test = ShoppingCart("one", 1)

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            test2 = ShoppingCart("O123", 1)

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_add_to_cart_product_price_equal_or_more_than_100(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.add_to_cart("Gold ball", 100)

        self.assertEqual("Product Gold ball cost too much!", str(ve.exception))

    def test_successful_add_to_cart(self):
        result = self.shopping_cart.add_to_cart("Carrots 2X", 4)
        self.assertEqual(4, self.shopping_cart.products["Carrots 2X"])
        self.assertEqual("Carrots 2X product was successfully added to the cart!", result)

    def test_removing_unexisting_product_from_cart(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.remove_from_cart("Potatoes")

        self.assertEqual("No product with name Potatoes in the cart!", str(ve.exception))

    def test_remove_product_from_cart(self):
        self.shopping_cart.products = {"Carrots 2X": 4}
        result = self.shopping_cart.remove_from_cart("Carrots 2X")
        self.assertEqual({}, self.shopping_cart.products)
        self.assertEqual("Product Carrots 2X was successfully removed from the cart!", result)

    def test_combining_shops(self):
        second_shop = ShoppingCart("Factory", 18.90)
        fantastico_factory = self.shopping_cart + second_shop
        self.assertEqual("ShoppingCart", type(fantastico_factory).__name__)
        self.assertEqual("FantasticoFactory", fantastico_factory.shop_name)
        self.assertEqual(35.40, fantastico_factory.budget)
        self.assertEqual({}, fantastico_factory.products)

    def test_unsuccessful_buy_products(self):
        self.shopping_cart.products = {"Carrot 7X": 26, "Lemonade": 3.40, "Bread": 1.50}

        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.buy_products()

        self.assertEqual("Not enough money to buy the products! Over budget with 14.40lv!", str(ve.exception))

    def test_successful_buy_products(self):
        self.shopping_cart.products = {"Milk": 2.45}
        result = self.shopping_cart.buy_products()
        self.assertEqual('Products were successfully bought! Total cost: 2.45lv.', result)


if __name__ == '__main__':
    main()
