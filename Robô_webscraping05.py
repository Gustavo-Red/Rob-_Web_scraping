#Contexto:
# Te contrataram para criar um robô que verifica se determinados domínios ja estão sendo usados, este robô verifica através do site https://registro.br/
# Obs: Será necessário a biblioteca Selenium








from selenium import webdriver # webdriver: É o robô que vai fazer as coisas na internet
from selenium.webdriver.chrome.service import Service # <-- necessário no Selenium
from selenium.webdriver.common.keys import Keys # selenium.webdriver.common.keys: parte da biblioteca selenium ,"Keys", que permite o programa usar o seu teclado.
from selenium.webdriver.common.by import By
import time
import xlrd # xlrd: biblioteca para mexer com planilhas do excel

print("\n")

print("Iniciando o robô...")

print("\n")

# open("[nome do arquivo de texto].txt", "w") é um comando para criar um arquivo de texto
arquivo = open("/home/gustavov/VSCODE/Projeto_Webscraping/resultado.txt", "w")

workbook = xlrd.open_workbook('/home/gustavov/VSCODE/Projeto_Webscraping/dominios.xls')
sheet = workbook.sheet_by_name('Domínios')
rows = sheet.nrows
columns = sheet.ncols

###########################################################################################################

service = Service('/home/gustavov/chromedriver-linux64/chromedriver')  # <-- caminho completo
driver = webdriver.Chrome(service=service) # <-- passa como service=, não como string

###########################################################################################################

#comando driver.get('[algum site]') irá fazer o robô abrir o site em questão

driver.get('https://registro.br/')
time.sleep(3)

for curr_row in range(1, rows):
    x = sheet.cell_value(curr_row, 0)
    # O comando driver.find_element(By.ID, "[ID]") seleciona algo da página
    pesquisa = driver.find_element(By.ID, "is-avail-field") 
    time.sleep(0.5)
    pesquisa.clear() # -> esse comando apaga tudo que tá escrito na area em questão
    time.sleep(0.5)
    pesquisa.send_keys(x) # -> esse comando insere a string na area em questão
    time.sleep(0.5)
    pesquisa.send_keys(Keys.RETURN) # -> esse comando é para dar ENTER

    time.sleep(0.5) # -> para dar tempo de carregar a página

    # O comando driver.find_element(By.XPATH, "[XPATH]") seleciona algo da página que está dentro de uma tag HTML
    disponivel = driver.find_element(By.XPATH, "/html/body/div/div/main/div/section/div[2]/div/p/span/strong")

    time.sleep(0.5)

    texto = f"O domínio {x} está como '{disponivel.text}' \n" # -> o disponivel.text é para puxar a parte de texto daquele HTML
    arquivo.write(texto)
    time.sleep(1) # --> faz o codigo pausar por 8 segundos
arquivo.close()
driver.close() # --> comando para fechar o navegador
