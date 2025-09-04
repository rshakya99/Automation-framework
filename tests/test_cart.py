import allure
from pages.shop_page import ShopPage
from pages.cart_page import CartPage


@allure.feature("Cart")
@allure.story("Add product to cart")
def test_add_product_to_cart(driver):
    shop = ShopPage(driver)
    cart = CartPage(driver)

    with allure.step("Open shop page"):
        shop.open()

    with allure.step("Add first product to cart"):
        shop.add_first_product_to_cart()

    with allure.step("Go to cart"):
        cart.open()

    with allure.step("Verify product is added to cart"):
        assert cart.is_product_in_cart(), "Cart is empty, product not added"


@allure.feature("Cart")
@allure.story("Remove product from cart")
def test_remove_product_from_cart(driver):
    shop = ShopPage(driver)
    cart = CartPage(driver)

    with allure.step("Open shop page"):
        shop.open()

    with allure.step("Add first product to cart"):
        shop.add_first_product_to_cart()

    with allure.step("Go to cart"):
        cart.open()

    with allure.step("Remove product from cart"):
        cart.remove_item()

    with allure.step("Verify cart is empty"):
        assert cart.is_cart_empty(), "Cart is not empty after removing product"
