from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# price = browser.find_element_by_id("price")
# x_text = price.text
# total_price = calc(x_text)

finish_price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR"))


button = browser.find_element_by_xpath("//button[text()='Забронировать']")
button.click()

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

number = browser.find_element_by_id("input_value")
x_text = number.text
answer = calc(x_text)

input = browser.find_element_by_id("answer")
input.send_keys(answer)

button = browser.find_element_by_xpath("//button[text()='Отправить']")
button.click()