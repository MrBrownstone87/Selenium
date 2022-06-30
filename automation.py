from selenium import webdriver #подключаем драйвер и несколько модулей
from selenium.webdriver.common.by import By
import time



driver = webdriver.Chrome('/Users/mrbrownstone87/Downloads/chromedriver') #подключаем драйвера для Хрома, указав директорию файла с драйвером
driver.maximize_window() #разворачиваем окно браузера 


driver.get('https://demoqa.com') #открываем сайт


time.sleep(1) #здесь и далее делаем паузы после каждого действия для наглядности
elements_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]/div') #находим нашу кнопку
driver.execute_script("arguments[0].scrollIntoView();", elements_button) #прокручиваем страницу до кнопки
time.sleep(1) #делаем паузу
elements_button.click() #жмем на кнопку "Elements"


time.sleep(1) #делаем паузу после предыдущего действия
checkbox_button = driver.find_element(By.XPATH, '//*[@id="item-1"]/span') #находим нашу кнопку "Check Box"
time.sleep(1) #делаем паузу
checkbox_button.click() #жмем на кнопку "Check Box"


time.sleep(1) #делаем паузу после предыдущего действия
home_checkbox_button = driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/span/label/span[3]') #находим чекбокс "Home"
time.sleep(1) #делаем паузу
home_checkbox_button.click() #проставляем чекбокс "Home"


time.sleep(1) #делаем паузу после предыдущего действия
radio_button = driver.find_element(By.XPATH, '//*[@id="item-2"]/span') #находим кнопку "Radio Button"
time.sleep(1) #делаем паузу
radio_button.click() #жмем кнопку "Radio Button"


time.sleep(1) #делаем паузу после предыдущего действия
impressive_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/label') #находим кнопку "Impressive"
time.sleep(1) #делаем паузу
impressive_button.click() #жмем на кнопку "Impressive"

time.sleep(1) #делаем паузу после предыдущего действия
yes_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[2]/label') #находим кнопку "Yes"
time.sleep(1) #делаем паузу
yes_button.click() #жмем на кнопку "Yes"
