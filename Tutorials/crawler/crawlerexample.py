import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from PIL import Image

# search_query = "tv"

# search_url = "https://www.amazon.in"




def crawler(search_query,search_url,name):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(search_url)

    # search_input = driver.find_element(By.CSS_SELECTOR,"input[name='#twotabsearchtextbox']")  
    search_input = driver.find_element(By.ID, "twotabsearchtextbox")

    search_input.clear()
    search_input.send_keys(search_query)
    search_input.send_keys(Keys.RETURN)
    time.sleep(5)
    screenshot_path = "images/"+name+".png"
    driver.save_screenshot(screenshot_path)

    if not os.path.exists("images"):
        os.makedirs("images")
    driver.quit()

    img = Image.open(screenshot_path)
    # cropped_img = img.crop((0, 70, img.width, img.height - 80))
    # cropped_img.save(screenshot_path)
    img.save(screenshot_path)

