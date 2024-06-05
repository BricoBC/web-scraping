import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import Select
import pandas as pd

try:   
    service = Service('D:\\Programas\\edgedriver_win64\\msedgedriver.exe')
    options = Options()

    driver = webdriver.Edge(service=service, options=options)
    website = 'https://www.adamchoi.co.uk/'

    driver.get(website)

    mult_s_team_goals = driver.find_element(By.XPATH, '//li[@ng-class="{active: sc.collapseVar === 8}"]') #Elemento padre
    mult_s_team_goals.click()
    time.sleep(1)

    btn_detailed = mult_s_team_goals.find_element(By.XPATH, '//a[@ui-sref="site.teamgoalsdetailed"]') #Elemento hijo
    btn_detailed.click()

    btn_all_match = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
    btn_all_match.click()   

    s_country =  Select(driver.find_element(By.ID, 'country'))
    time.sleep(1)
    s_country.select_by_visible_text('Mexico')

    matches = driver.find_elements(By.TAG_NAME, 'tr')
    liga_mx = []
    for match in matches:
        print(match.text)
        liga_mx.append(match.text)


# except:
#     print("Vuelvelo a ejecutar...")

finally:
    time.sleep(3)  # tiempo implicito: detener el proceso por n segundos
    driver.quit()
