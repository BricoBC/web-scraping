from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options


service = Service('D:\\Programas\\edgedriver_win64\\msedgedriver.exe')
options = Options()

driver = webdriver.Edge(service=service, options=options)
website = 'https://www.adamchoi.co.uk/'

driver.get(website)

