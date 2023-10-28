from random import randint

from selenium.webdriver.common.by import By

from tests.pages.Page import Page


class ProductPage(Page):

    url = "https://www.saucedemo.com/inventory.html"

    def __init__(self, driver):
        super().__init__(self.url, driver)

    def is_logged(self):
        return self.driver.find_element(By.ID, "react-burger-menu-btn").is_displayed()

    def add_random_product_to_cart(self):
        product = self._get_products()
        add_to_cart_btn = product.find_element(By.CLASS_NAME, "btn_primary")
        if add_to_cart_btn.text != "Add to cart":
            raise Exception("Add to cart button name is invalid!")
        add_to_cart_btn.click()

        remove_btn = product.find_element(By.CLASS_NAME, "btn_secondary")
        if remove_btn.text != "Remove":
            raise Exception("Remove button name is invalid!")

        product_name = product.find_element(By.CLASS_NAME, "inventory_item_name ").text

        return product_name

    def _get_products(self):
        products_list = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        random_index = randint(0, len(products_list) - 1)
        return products_list[random_index]

    def get_cart_total_items(self):
        return int(self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text)

    def open_cart_page(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()