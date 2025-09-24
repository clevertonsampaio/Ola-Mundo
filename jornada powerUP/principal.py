import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5

#passo 1: Entrar no sistema da empresa (chrome)
#abrir o chrome 
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(2)


pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# esperar 3 segundos
time.sleep(5)

#passo 2: Fazer login no sistema
pyautogui.click(x=752, y=690) # clicar no campo de email
pyautogui.write('tom.tom@tom.com') # escrever o email

# prencher a senha 
pyautogui.press('tab') # apertar tab  
pyautogui.write('123456') # escrever a senha

#botao logar
pyautogui.press('tab') # apertar tab
pyautogui.press('enter') # apertar enter para entrar no sistema

# espera de 3s
time.sleep(3)

#passo 3: importar a base de dados
tabela = pd.read_csv('produtos.csv')

#passo 4: cadastrar 1 produto
time.sleep(3)
pyautogui.click(x=1217, y=538) 

for linha in tabela.index:
    pyautogui.click(x=610, y=513)

    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab')

    marca = tabela.loc[linha, 'marca']  
    pyautogui.write(marca)
    pyautogui.press('tab')

    tipo = tabela.loc[linha, 'tipo']    
    pyautogui.write(tipo)
    pyautogui.press('tab')

    categoria = str(tabela.loc[linha, 'categoria'])     
    pyautogui.write(categoria)
    pyautogui.press('tab')

    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])    
    pyautogui.write(preco_unitario)
    pyautogui.press('tab')

    custo = str(tabela.loc[linha, 'custo'])  
    pyautogui.write(custo)
    pyautogui.press('tab')

    obs = str(tabela.loc[linha, 'obs'])  
    if obs != 'nan':
        pyautogui.write(obs)    
    pyautogui.press('tab')

    pyautogui.press('enter')

    pyautogui.scroll(1000)
#passo5: repetir para todos os produtos

#pyautogui -> fazer automaçoes com python

