from lib2to3.pgen2 import driver
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import pandas as pd
import requests
import time
import csv
from random import randint
#-----------------------proceso 1 notebooks----------------#
lista2 = []

count = 1

while count < 4:
 
    url = 'https://www.pcfactory.cl/notebooks?categoria=735&papa=636&pagina='+ str(count)

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html5lib')

    categorias = soup.find_all("div", {"class": "product"})

    if count > 3:
     break
    count = count + 1
     
    for categoria in categorias:
        marca = categoria.find("div", {"class": "product__heading"})
        modelo = categoria.find("div", {"class": "p-relative"})
        precio = categoria.find("div", {"class": "product__price"})
        print(marca.text + "  ##  " + modelo.text + "  ## " + "  ##  " + precio.text)
        lista = [marca.text, modelo.text,  precio.text]
        lista2.append(lista)


lista3 = pd.DataFrame(lista2)

lista3.to_excel("notebooks.xlsx")


#-----------------------proceso 2 celulares----------------#
lista2 = []

count = 1

while count < 7:

    url = 'https://www.pcfactory.cl/smartphones?categoria=5&papa=645&pagina='+ str(count)

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html5lib')

    categorias = soup.find_all("div", {"class": "product"})

    if count > 6:
     break
    count = count + 1
     
    for categoria in categorias:
        marca = categoria.find("div", {"class": "product__heading"})
        modelo = categoria.find("div", {"class": "p-relative"})
        precio = categoria.find("div", {"class": "product__price"})
        print(marca.text + "  ##  " + modelo.text + "  ## " + "  ##  " + precio.text)
        lista = [marca.text, modelo.text,  precio.text]
        lista2.append(lista)


lista3 = pd.DataFrame(lista2)

lista3.to_excel("celulares.xlsx")

#-----------------------proceso 3 consolas----------------#
lista2 = []

count = 1

while count < 2:

    url = 'https://www.pcfactory.cl/consolas?categoria=438&papa=374&pagina='+ str(count)

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html5lib')

    categorias = soup.find_all("div", {"class": "product"})

    if count > 1:
     break
    count = count + 1
     
    for categoria in categorias:
        marca = categoria.find("div", {"class": "product__heading"})
        modelo = categoria.find("div", {"class": "p-relative"})
        precio = categoria.find("div", {"class": "product__price"})
        print(marca.text + "  ##  " + modelo.text + "  ## " + "  ##  " + precio.text)
        lista = [marca.text, modelo.text,  precio.text]
        lista2.append(lista)


lista3 = pd.DataFrame(lista2)

lista3.to_excel("consolas.xlsx")