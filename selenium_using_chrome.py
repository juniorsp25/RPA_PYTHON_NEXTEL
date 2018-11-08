from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json
from pprint import pprint
import time


class GoogleSearchRpa:

    pesquisa_google = []

#read file

def pega_dados(obj):
    instancia = meuprograma.google-me(
        nextel = obj['nextel'],
        telefonia_do_futuro = obj['telefonia do futuro'],
        selenium_python = obj['selenium python']
      )
    return instancia

try:
    arquivo_json = open('output.json','r')
    dados_json = json.load(arquivo_json)
    pesquisa_google = dados_json['google-me']

    pesquisa_google = [pega_dados(Pesquisar) for pesquisar in pesquisa_google ]
except Exception as erro:
    
    print("\n",pesquisa_google)

#search keywords in browser
    
driver = webdriver.Chrome()
print("\n",'###############print keywords file output.json################')
for acessar in pesquisa_google:
    driver.get('http://www.google.com.br')
    driver.find_element_by_name('q').send_keys(acessar,)
    driver.find_element_by_name('btnK').send_keys(Keys.ENTER)

    
    print("\n",acessar)
    #driver.close()









