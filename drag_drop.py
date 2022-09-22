from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r"D:\User\Anahi\Documents\Escuela\SEMESTRE_7\SQA\chromedriver.exe")
action = ActionChains(driver)
url = "http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html"

driver.maximize_window()
driver.get(url)
time.sleep(3)

oslo = driver.find_element(By.ID,"box1")
noreway = driver.find_element(By.ID,"box101")
action.drag_and_drop(oslo, noreway).perform()
time.sleep(1)

sweden = driver.find_element(By.ID,"box2")
stockholm = driver.find_element(By.ID,"box102")
action.drag_and_drop(sweden, stockholm).perform()
time.sleep(1)

usa = driver.find_element(By.ID,"box3")
washington = driver.find_element(By.ID,"box103")
action.drag_and_drop(usa, washington).perform()
time.sleep(1)

denmark= driver.find_element(By.ID,"box4")
copenhagen = driver.find_element(By.ID,"box104")
action.drag_and_drop(denmark, copenhagen).perform()
time.sleep(1)

sk = driver.find_element(By.ID,"box5")
seoul = driver.find_element(By.ID,"box105")
action.drag_and_drop(sk, seoul).perform()
time.sleep(1)

italy = driver.find_element(By.ID,"box6")
rome = driver.find_element(By.ID,"box106")
action.drag_and_drop(italy, rome).perform()
time.sleep(1)

spain = driver.find_element(By.ID,"box7")
madrid = driver.find_element(By.ID,"box107")
action.drag_and_drop(spain, madrid).perform()
time.sleep(1)

driver.quit()