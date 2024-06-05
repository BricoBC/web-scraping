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

    btn_win = driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[13]/a')
    btn_win.click()

    
finally:
    time.sleep(5) 
    driver.quit()
