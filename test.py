import unittest
import surf
import datetime

class SurfShopTests(unittest.TestCase):

    def setUp(self):
        self.cart = surf.ShoppingCart()

    def test_add_surfboard(self):
        message = self.cart.add_surfboards(quantity=1)
        self.assertEqual(message, f'Successfully added 1 surfboard to cart!')

    def test_add_surfboards(self):
        for i in range(2, 5):
            with self.subTest(i=i):
                message = self.cart.add_surfboards(i)
                self.assertEqual(message, f'Successfully added {i} surfboards to cart!')
                self.cart = surf.ShoppingCart()

    @unittest.skip
    def test_add_too_many_surfboards(self):
        self.assertRaises(surf.TooManyBoardsError, self.cart.add_surfboards, 5)

    def test_apply_locals_discount(self):
        self.cart.apply_locals_discount()
        self.assertTrue(self.cart.locals_discount)

    def test_add_invalid_checkout_date(self):
        date = datetime.datetime.now()
        self.assertRaises(surf.CheckoutDateError, self.cart.set_checkout_date, date)


unittest.main()