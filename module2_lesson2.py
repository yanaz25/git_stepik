import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/selects1.html")

x = int(browser.find_element(By.ID, "num1").text)
y = int(browser.find_element(By.ID, "num2").text)
result = x + y

select = Select(browser.find_element(By.ID, "dropdown"))
select.select_by_value(str(result))
browser.find_element(By.XPATH, "//*[@type='submit']").click()

time.sleep(5)
browser.quit()