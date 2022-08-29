from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:/Users/oakinola/Downloads/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie=driver.find_element(By.ID,"cookie")
cursor=driver.find_element(By.ID,'buyCursor')
grandma=driver.find_element(By.ID,'buyGrandma')
factory=driver.find_element(By.ID,'buyFactory')
mine=driver.find_element(By.ID,"buyMine")
shipment=driver.find_element(By.ID,"buyShipment")
alchemy_lab=driver.find_element(By.ID,"buyAlchemy lab")
Score=driver.find_element(By.ID,"money").text
print(driver.find_element(By.XPATH,'//*[@id="buyCursor"]/b').text)
start_time=time.time()
timeout = time.time() + 1
play=True
while play:

    cookie.click()
    if int(driver.find_element(By.ID,"money").text) > int(driver.find_element(By.XPATH, '//*[@id="buyGrandma"]/b').text.split()[2]):
        driver.find_element(By.ID, 'buyGrandma').click()
    if int(driver.find_element(By.ID,"money").text) > int(driver.find_element(By.XPATH, '//*[@id="buyCursor"]/b').text.split()[2]):
        driver.find_element(By.ID,'buyCursor').click()
    # elif int(driver.find_element(By.ID,"money").text) > int(driver.find_element(By.XPATH, '//*[@id="buyFactory"]/b').text.split()[2]):
    #     driver.find_element(By.ID,'buyFactory').click()

    if time.time() == 5 * 60:
        play = False
