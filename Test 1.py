# Importar Librerías    

from fileinput import close
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
#from time import sleep
import random
import pandas as pd
from selenium.webdriver.common.keys import Keys
import time
import traceback

# Ruta de  navegación
try:  
   Chrome_driver =  webdriver.Chrome("C:\\Users\FRANCISCO\Downloads\chromedriver.exe")

# Iniciador del Navegador

   Chrome_driver.get("https://www.solotodo.cl/")

   Chrome_driver.get("https://www.solotodo.cl/cells")

# Buscar elementos navegador 

   buscador_ventana = Chrome_driver.find_element_by_id('searcher')
   buscador_ventana.send_keys('Apple iphone') 

#buscador_ventana = Chrome_driver.find_element_by_xpath('//*[@id="navbar"]/div/ul[2]/div/form/div/div/div/button/i')
   buscador_ventana.send_keys(Keys.ENTER)
   time.sleep(10) 


   equipos = Chrome_driver.find_elements_by_tag_name('h3')
   valor = Chrome_driver.find_elements_by_xpath("//div[contains(@class,'d-flex flex-column category-browse-result')]")

   for x in valor:
       print(x.text)

#for equipo in equipos:
 #print('Informacion ' + str(equipo.text))
   Chrome_driver.close()  

except Exception as e:
        print(e)
        traceback.print_exc()












#buscador_list = []

 #for producto in Chrome_driver:
    
    #title = Chrome_driver.find_element_by_link_text('.//*[@id="filters-and-results"]/div/div/div[1]/div[2]/div/div[1]/h3/a').text
    #store = Chrome_driver.find_element_by_xpath('.//*[@id="filters-and-results"]/div/div/div[1]/div[2]/div/div[1]/div[2]/dl/dd[3]').text
    #value = Chrome_driver.find_element_by_xpath('.//*[@id="filters-and-results"]/div/div/div[1]/div[2]/div/div[1]/div[3]/div/a').text
    
    #product_item = {
       # 'title': title,
        #'store': store,
        #'value': value
        #}

    #buscador_list.append(product_item)
    #df = pd.DataFrame(buscador_list)
    #print(df)