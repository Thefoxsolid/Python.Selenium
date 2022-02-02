# Importar Librerías    

from lib2to3.pgen2 import driver
from ssl import Options
from telnetlib import EC
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Opciones de navegación

Options = webdriver.ChromeOptions()
Options.add_argument('--star-maximized')
Options.add_argument('--disable-extensions')


Chrome_driver =  webdriver.Chrome("C:\\Users\FRANCISCO\Downloads\chromedriver.exe")

# Iniciador del Navegador

Chrome_driver.get("https://www.solotodo.cl/")

Chrome_driver.get("https://www.solotodo.cl/cells")


# Buscar elementos navegador 

WebDriverWait(driver,5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'search#inputSearch'))).send_keys('Apple')
    



 