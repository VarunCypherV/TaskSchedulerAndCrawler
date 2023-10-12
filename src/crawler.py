import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image

search_query = "leo trailer"

search_url = "https://www.youtube.com"

driver = webdriver.Chrome()

driver.get(search_url)

search_input = driver.find_element(By.CSS_SELECTOR,"input[name='search_query']")  # Using a CSS selector
search_input.clear()
search_input.send_keys(search_query)
search_input.send_keys(Keys.RETURN)

time.sleep(5)
screenshot_path = "images/screenshot.png"
driver.save_screenshot(screenshot_path)

if not os.path.exists("images"):
    os.makedirs("images")
driver.quit()

img = Image.open(screenshot_path)
cropped_img = img.crop((0, 70, img.width, img.height - 80))
cropped_img.save(screenshot_path)

