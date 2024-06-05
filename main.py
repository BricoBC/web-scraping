import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import Select

try:   
    service = Service('D:\\Programas\\edgedriver_win64\\msedgedriver.exe')
    options = Options()

    driver = webdriver.Edge(service=service, options=options)
    website = 'https://www.adamchoi.co.uk/'

    driver.get(website)

    btn_team_goals = driver.find_element(By.XPATH, '//li[@ng-class="{active: sc.collapseVar === 8}"]')
    btn_team_goals.click()

    btn_detailed = driver.find_element(By.XPATH, '//a[@ui-sref="site.teamgoalsdetailed"]')
    btn_detailed.click()

    btn_all_match = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
    btn_all_match.click()
    
    s_country =  Select(driver.find_element(By.ID, 'country'))

    # s_country = Select(driver.find_element(By.ID, 'countrySelect'))
    s_country.select_by_visible_text('Mexico')


finally:
    time.sleep(5) 
    driver.quit()
