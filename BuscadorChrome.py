# Importar Librerías    

from lib2to3.pgen2 import driver
from pathlib import Path
from ssl import Options
from telnetlib import EC
from tkinter.ttk import OptionMenu
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
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

buscador_ventana = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/nav/div/ul[2]/div/form/div/div/input')
buscador_ventana.send_keys('Apple')








 