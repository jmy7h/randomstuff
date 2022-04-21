import json
import time
from selenium import webdriver
from time import sleep
from resolution import pw
from resolution import un
from resolution import unt1
from resolution  import path


PATH = path

# path, username, password and target username in resolution.py

driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com/accounts/login")
sleep(1)
driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
sleep(1)
driver.find_element_by_xpath(
    '/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input').send_keys(un)
sleep(1)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(pw)
sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button/div').click()
sleep(10)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
sleep(5)
driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
driver.get(f"https://www.instagram.com/{unt1}")
sleep(1)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/div/span').click()
sleep(3)


popup = driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]")
container = driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div")
total_children = 0
time_since_last_children_increase = 0
timer_start = time.time()
while time_since_last_children_increase < 10:
    element = container.find_elements_by_xpath("./*")[-1]
    try:
        driver.execute_script("return arguments[0].scrollIntoView();", element)
    except:
        pass
 

current_children = len(container.find_elements_by_xpath("./*"))
    if len(container.find_elements_by_xpath("./*")) > total_children:
        total_children = current_children
        timer_start = time.time()
        time_since_last_children_increase = 0
    else:
        time_since_last_children_increase = time.time() - timer_start

accs = []
for elm in container.find_elements_by_xpath("./*"):
    username = elm.find_element_by_xpath("div/div[1]/div[2]/div[1]/span/a/span").text
    name = elm.find_element_by_xpath("div/div[1]/div[2]/div[2]").text
    accs.append(username)
print(accs)
with open('list1.json', 'w') as f:
    json.dump(accs, f)
print('code executed')
