import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from PIL import Image
from mailsender import sendEmail

def crawlerImage(reportName,search_url,name,email):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(search_url)

    search_input = driver.find_element(By.ID, "twotabsearchtextbox")

    search_input.clear()
    search_input.send_keys(reportName)
    search_input.send_keys(Keys.RETURN)
    time.sleep(5)
    screenshot_path = "images/"+name+"_"+reportName+".png"
    driver.save_screenshot(screenshot_path)
    #Checking folder existancer to save image
    if not os.path.exists("images"):
        os.makedirs("images")
    driver.quit()
    #PIL saving the image
    img = Image.open(screenshot_path)
    img.save(screenshot_path)
    sendEmail(screenshot_path,email)
    driver.quit()

def crawlerContent(reportName, search_url, name,email):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(search_url)

    search_input = driver.find_element(By.ID, "twotabsearchtextbox")
    search_input.clear()
    search_input.send_keys(reportName)
    search_input.send_keys(Keys.RETURN)
    time.sleep(5)

    # Find all elements with the class "a-text-normal"
    elements = driver.find_elements(By.CLASS_NAME, "a-text-normal")

    text_folder_path = "Text"
    text_file_path = f"{text_folder_path}/{name}.txt"

    with open(text_file_path, 'w', encoding='utf-8') as file:
        for element in elements:
            file.write(element.text + '\n')

    sendEmail(text_file_path,email)
    driver.quit()
    