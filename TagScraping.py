#  coding=gbk
from selenium import webdriver
from selenium.webdriver.common.by import By
import clipboard


def tag_scraping(name):
    driver = webdriver.Chrome(executable_path="/Users/soeren/bin/chromedriver")

    driver.get('https://rapidtags.io/generator')
    search_box = driver.find_element(By.XPATH, '//*[@id="searchInput"]')
    driver.implicitly_wait(10)
    search_box.send_keys(name)
# accept cockies
    search_cockie_button = driver.find_element(By.XPATH, '//*[@id="agree"]')
    search_cockie_button.click()
# click search button
    search_button = driver.find_element(By.XPATH, '//*[@id="search-wrapper"]/div[1]/label/button')
    search_button.click()
# wait (prevents failing if bad internet connection)
    driver.implicitly_wait(10)
# click copy button
    copy_button = driver.find_element(By.XPATH, '//*[@id="tag-generator"]/div[2]/button')
    copy_button.click()
# pasting into clipboard
    tags = clipboard.paste()

    return tags
