from utilities.driver_setup import get_driver
from pages.inventory_page import InventoryPage

import random
import time

# Step 1: Operate Browser
driver = get_driver()

# Step 2: Open the Website
driver.get("https://tutorialsninja.com/demo/")

#Step 3: Inventory Page
inventory = InventoryPage(driver)

#Step 4: Click on Phones & PDAs
inventory.upper_tab()

# Step 5: Assertion of page
product_page = inventory.get_product()

assert product_page == "Phones & PDAs", "❌ Failed to load Next Page"
print("✅ Phones & PDAs Page loaded successfully")

# Step 6: Click on product
inventory.iphone_click()
time.sleep(3)

# Step 7: Click on image
inventory.click_pic() #1
time.sleep(1)

# Step 8: Click on next image
for i in range(0, 5):
    inventory.click_next()
    time.sleep(2)

# Step 9: Save Screenshot
driver.save_screenshot('screenshot#' + str(random.randint(0, 101)) + '.png')

# Step 10: close the image
inventory.x_button()
time.sleep(2)

# Step 11: remove 1 and add 2 in product textbox
inventory.rem_qty()
inventory.add_qty()
time.sleep(1)

# Step 12: Add to cart
inventory.add_to_cart()
time.sleep(2)

# Step 13: Check if assertion is correct, thsi formula will check substring
asserted_iphone = inventory.assertion_iphone()
assert "Success: You have added" in asserted_iphone, "❌ Product not added to cart"
print("✅ Your Product added to cart successfully")
time.sleep(2)

# Step 14: click on laptop
inventory.tab_laptop()
time.sleep(1)
inventory.all_laptop()
time.sleep(1)
inventory.macbook()
time.sleep(1)
inventory.add_to_cart()
time.sleep(1)

# Step 15: drag down and click
inventory.mp3_dropdown()
time.sleep(1)
inventory.all_mp3()
time.sleep(1)
inventory.scroll_ipod()
time.sleep(1)
inventory.ipod()
time.sleep(1)
inventory.add_to_cart()
time.sleep(1)

#Step 16: click on cart remove 1 product
inventory.cart()
time.sleep(2)
inventory.rem_product()
time.sleep(1)

#step 17: Click in View Cart
inventory.cart()
time.sleep(1)
inventory.view_cart()
time.sleep(1)
asserted_cart = inventory.alert()
assert "Products marked with" in asserted_cart, "❌ Error not found"
print("✅ Error Message Found")