import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

try:   
    service = Service('D:\\Programas\\edgedriver_win64\\msedgedriver.exe')

    driver = webdriver.Edge(service=service)
    website = 'https://www.adamchoi.co.uk/'

    driver.get(website)

    wait = WebDriverWait(driver, 10)

    mult_s_team_goals = wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@ng-class="{active: sc.collapseVar === 8}"]')))
    mult_s_team_goals.click()


    btn_detailed = mult_s_team_goals.find_element(By.XPATH, '//a[@ui-sref="site.teamgoalsdetailed"]') #Elemento hijo)
    btn_detailed.click()

    btn_all_match = wait.until(EC.visibility_of_element_located((By.XPATH, '//label[@analytics-event="All matches"]')))
    btn_all_match.click()  

    s_country = wait.until(EC.visibility_of_element_located((By.ID, 'country')))
    select_country = Select(s_country)
    # s_country =  Select(driver.find_element(By.ID, 'country'))
    select_country.select_by_visible_text('Mexico')

    matches = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'tr')))
    liga_mx = []
    for match in matches:
        print(match.text)
        liga_mx.append(match.text)

    df = pd.DataFrame({'Liga MX': liga_mx})
    df.to_csv('players.csv',index=False)
except:
    print("Vuelvelo a ejecutar...")

finally:
    time.sleep(3)  # tiempo implicito: detener el proceso por n segundos
    driver.quit()
