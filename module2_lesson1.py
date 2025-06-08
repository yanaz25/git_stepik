import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")
x_element = browser.find_element(By.ID, "treasure")

x = int(x_element.get_attribute("valuex"))
y = calc(x)

browser.find_element(By.ID, "answer").send_keys(y)
browser.find_element(By.ID, "robotCheckbox").click()
browser.find_element(By.ID, "robotsRule").click()
browser.find_element(By.XPATH, "//*[@type='submit']").click()

time.sleep(5)
browser.quit()
