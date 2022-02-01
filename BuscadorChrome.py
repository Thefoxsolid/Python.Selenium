# Importar Librerías    

from lib2to3.pgen2 import driver
import unittest
from webbrowser import Chrome
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

Chrome_driver =  webdriver.Chrome("C:\\Users\FRANCISCO\Downloads\chromedriver.exe")
Chrome_driver.get("https://www.solotodo.cl/")

Chrome_driver.get("https://www.solotodo.cl/cells")

print(driver.title)

search_bar = driver.find_element_by_name("cells")

# lista de productos

celular = driver.find_element_by_class_name("class= css-16pqwjk-indicatorContainer")

celular = driver.find_element_by_class_name("class= css-12jo7m5")



 