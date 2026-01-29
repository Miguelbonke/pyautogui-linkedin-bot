import pyautogui
import time

# Tempo de pausa entre as ações
pyautogui.PAUSE = 1.5

print("Abrindo o menu iniciar...")
pyautogui.press('win')
pyautogui.write('Google Chrome')
pyautogui.press('enter')

# Aguarda o navegador abrir
time.sleep(5)

print("Acessando o LinkedIn...")
pyautogui.write(
    'https://www.linkedin.com/login/pt?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
)
pyautogui.press('enter')

# Aguarda a página carregar
time.sleep(5)

print("Pesquisando vagas de Estágio em TI...")
pyautogui.click(x=307, y=114)
pyautogui.write('Estágio TI')
pyautogui.press('enter')

# Clique em resultado/filtro
pyautogui.click(x=820, y=668)

print("Automação finalizada.")
