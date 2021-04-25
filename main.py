import random
import time

from selenium import webdriver

driver = webdriver.Chrome("D:/Pobrane/chromedriver.exe")

driver.get("https://www.ea.com/pl-pl/fifa/ultimate-team/web-app/")
time.sleep(5)
button = driver.find_element_by_class_name("btn-standard.call-to-action")
button.click()
time.sleep(2)
input = driver.find_element_by_name("email")
input.send_keys("xxx")
input = driver.find_element_by_name("password")
input.send_keys("xxx")
button = driver.find_element_by_id("btnLogin")
button.click()
time.sleep(40)

x = 0
driver.find_element_by_class_name("ut-tab-bar-item.icon-transfer").click()
time.sleep(5)
driver.find_element_by_class_name("tile.col-1-1.ut-tile-transfer-market").click()

while True:
    try:
        time.sleep(1)
        cena = driver.find_elements_by_class_name("numericInput")
        if x%2 == 0:
            kwota = "3000"
            player = "Sissoko"
        elif x%2 == 1:
            kwota = "3000"
            player = "Davinson"

        x = x + 1
        cena[3].clear()
        cena[3].send_keys(kwota)
        driver.find_element_by_class_name("ut-text-input-control").clear()
        driver.find_element_by_class_name("ut-text-input-control").send_keys(player)
        time.sleep(1)
        players = driver.find_element_by_class_name("btn-text").click()
        time.sleep(0.2)
        driver.find_element_by_class_name("btn-standard.call-to-action").click()
        time.sleep(1.5)
        try:
            driver.find_element_by_class_name("btn-standard.buyButton.currency-coins").click()
            time.sleep(1)
            if driver.find_elements_by_class_name("btn-text")[3].text == "PRZEJDŹ":
                driver.find_elements_by_class_name("btn-text")[3].click()
                time.sleep(random.randint(1, 2))
                driver.find_element_by_class_name("btn-standard.section-header-btn.mini.call-to-action").click()
                time.sleep(random.randint(1, 2))
                driver.find_elements_by_class_name("btn-text")[12].click()
                driver.find_element_by_class_name("ut-navigation-button-control").click()
            elif driver.find_elements_by_class_name("btn-text")[2].text == "OK":
                driver.find_elements_by_class_name("btn-text")[2].click()
                time.sleep(random.randint(1, 2))
                driver.find_element_by_class_name("ut-navigation-button-control").click()
            else:
                driver.find_element_by_class_name("ut-navigation-button-control").click()
        except:
            time.sleep(random.randint(1, 2))
            driver.find_element_by_class_name("ut-navigation-button-control").click()
    except:
        pass
