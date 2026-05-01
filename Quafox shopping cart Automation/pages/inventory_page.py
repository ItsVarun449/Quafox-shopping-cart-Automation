from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InventoryPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    phone = (By.XPATH, '//a[text() = "Phones & PDAs"]')
    def upper_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.phone)).click()

    Product_Category = (By.XPATH, '//h2[text() = "Phones & PDAs"]')

    def get_product(self):
        return self.wait.until(EC.visibility_of_element_located(self.Product_Category)).text
    
    iphones = (By.XPATH, '//a[text() = "iPhone"]')

    def iphone_click(self):
        self.wait.until(EC.element_to_be_clickable(self.iphones)).click()

    first_pic = (By.XPATH, '(//ul[@class = "thumbnails"]//li)[1]')

    def click_pic(self):
        self.wait.until(EC.element_to_be_clickable(self.first_pic)).click()

    next_click = (By.XPATH,'//button[@title = "Next (Right arrow key)"]')

    def click_next(self):
        self.wait.until(EC.element_to_be_clickable(self.next_click)).click()
    
    close_button = (By.XPATH, '//button[@title = "Close (Esc)"]')

    def x_button(self):
        self.wait.until(EC.element_to_be_clickable(self.close_button)).click()

    text_input = (By.ID, 'input-quantity')

    def rem_qty(self):
        self.wait.until(EC.element_to_be_clickable(self.text_input)).clear()

    text_input_add = (By.ID, 'input-quantity')

    def add_qty(self):
        self.wait.until(EC.element_to_be_clickable(self.text_input_add)).send_keys('2')

    cart_add = (By.ID, 'button-cart')
    def add_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.cart_add)).click()

    asserted_product = (By.XPATH, '//div[contains(text(), "Success: You have added")]')
    def assertion_iphone(self):
        return self.wait.until(EC.visibility_of_element_located(self.asserted_product)).text
    
    laptop_tab = (By.XPATH, '(//a[@class = "dropdown-toggle"])[3]')
    def tab_laptop(self):
        self.wait.until(EC.element_to_be_clickable(self.laptop_tab)).click()

    show_all_laptop = (By.XPATH, '//a[text() = "Show AllLaptops & Notebooks"]')
    def all_laptop(self):
        self.wait.until(EC.element_to_be_clickable(self.show_all_laptop)).click()

    select_macbook = (By.XPATH, '//a[text() = "MacBook"]')
    def macbook(self):
        self.wait.until(EC.element_to_be_clickable(self.select_macbook)).click()

    click_mp3_dropdown = (By.XPATH, '//a[text() = "MP3 Players"]')
    def mp3_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.click_mp3_dropdown)).click()

    show_all_mp3 = (By.XPATH, '//a[text() = "Show AllMP3 Players"]')
    def all_mp3(self):
        self.wait.until(EC.element_to_be_clickable(self.show_all_mp3)).click()
    
    scroll_down_ipod = (By.XPATH, '//img[@title = "iPod Touch"]')
    def scroll_ipod(self):
        self.wait.until(EC.visibility_of_element_located(self.scroll_down_ipod)).location_once_scrolled_into_view

    select_ipod = (By.XPATH, '//a[text() = "iPod Touch"]')
    def ipod(self):
        self.wait.until(EC.element_to_be_clickable(self.select_ipod)).click()

    select_cart = (By.ID, "cart-total")
    def cart(self):
        self.wait.until(EC.element_to_be_clickable(self.select_cart)).click()

    cancel_product = (By.XPATH, '(//button[@title = "Remove"])[2]')
    def rem_product(self):
        self.wait.until(EC.element_to_be_clickable(self.cancel_product)).click()

    Cart_view = (By.XPATH, '//strong[text() = "View Cart"]')
    def view_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.Cart_view)).click()

    checkout_message = (By.XPATH, '//div[contains(text(), "Products marked with")]')
    def alert(self):
        return self.wait.until(EC.visibility_of_element_located(self.checkout_message)).text