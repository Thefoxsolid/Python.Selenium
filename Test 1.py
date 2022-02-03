# Importar Librerías    

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import random

# Ruta de  navegación

Chrome_driver =  webdriver.Chrome("C:\\Users\FRANCISCO\Downloads\chromedriver.exe")

# Iniciador del Navegador

Chrome_driver.get("https://www.solotodo.cl/")

Chrome_driver.get("https://www.solotodo.cl/cells")

# Buscar elementos navegador 

buscador_ventana = Chrome_driver.find_element_by_id('searcher')
buscador_ventana.send_keys('Apple iphone') 

buscador_ventana = Chrome_driver.find_element_by_xpath('//*[@id="navbar"]/div/ul[2]/div/form/div/div/div/button/i')
buscador_ventana.click() 




