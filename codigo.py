import pyautogui
import time

pyautogui.PAUSE = 0.3
pyautogui.FAILSAFE = True


pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)


# Fazer login
# selecionar o campo de email

pyautogui.click(x=1598, y=380)

# Email
pyautogui.write("mbmgomes00234@gmail.com")
pyautogui.press("tab") 
pyautogui.write("12345")
pyautogui.click(x=955, y=638) 
time.sleep(3)

# Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

# Cadastrar um produto
for linha in tabela.index:
    pyautogui.click(x=1442, y=260)
    
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")  

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000)
