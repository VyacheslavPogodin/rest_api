import pytest
from time import sleep, time
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select

from selenium.webdriver.chrome.service import Service



url = 'http://10.10.29.110/login'
login = 'user_admin'
password = 'admin123'
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#options.add_argument("--headless")

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(10)

def autenification(url, metod): #Аутентификация на сайте
    
    metod.get(url)
    metod.find_element(By.NAME, 'login').send_keys(login)
    metod.find_element(By.NAME, 'password').send_keys(password)
    metod.find_element(By.TAG_NAME, 'button').click()
    return metod


class TestWeb():

    def test_page_uspd_config(self):  # Проверяем наличие названия пунктов записей на странице

        page_step = autenification(url, driver)
        sleep(2)

        # Cписок названий пунктов
        list_name = ('Наименование',
            'Модификация',
            'Заводской номер',
            'Адрес',
            'Метрологический модуль (ММ)',
            'MD5 хэш ММ',
            'Версия конфигуратора',
            #'Бестолковка',
            )



        for name in list_name:
            assert name in  page_step.page_source, f"Пункт с наименованием {name} отсуствует"
        


if __name__ == '__main__':

    page_step = autenification(url, driver)
    sleep(3)
    # page_step.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div[3]/ul/li[1]').click()
    
    # if page_step.find_element(By.XPATH, '//*[@id="simple-tabpanel-0"]/div/div[1]/table/div/div/span/span[1]').get_attribute('class') == 'MuiSwitch-switchBase MuiSwitch-colorPrimary MuiButtonBase-root MuiSwitch-switchBase MuiSwitch-colorPrimary PrivateSwitchBase-root css-svzrxe':
    
    #     page_step.find_element(By.XPATH, '//*[@id="simple-tabpanel-0"]/div/div[1]/table/div/div/span/span[1]/input').click()
    
    # page_step.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div[2]/ul/li[2]').click()
    # page_step.find_element(By.XPATH, '//*[@id="root"]/div[2]/main/div[2]/div/div[1]/button').click()


    # page_step.find_element(By.XPATH, '//*[@id="root"]/div[2]/main/div[2]/fieldset/div/label[1]/span[1]/input').click()
    
    page_step.get('http://10.10.29.110/devices/add')

    page_step.find_element(By.NAME, 'a').send_keys("123")
    
    # page_step.find_element(By.NAME, 'b').click()
    # page_step.find_element(By.NAME, 'b').send_keys(Keys.ARROW_DOWN * 4 + Keys.ENTER)
    # page_step.find_element(By.NAME, 'b').click()
    
    # page_step.find_element(By.NAME, 'c').send_keys('123456789')
    # page_step.find_element(By.NAME, 'd').send_keys('123456789ABCDEF0')
    
    # page_step.find_element(By.NAME, 'h').click()
    # page_step.find_element(By.NAME, 'j').click()
    # page_step.find_element(By.NAME, 'k').click()
    # page_step.find_element(By.NAME, 'l').click()
    # page_step.find_element(By.NAME, 'm').click()

    # # page_step.find_element(By.NAME, 'g').click()
    # # page_step.find_element(By.NAME, 'g').send_keys(Keys.ARROW_DOWN + Keys.ENTER)
    # # page_step.find_element(By.NAME, 'g').click()

    # page_step.find_element(By.NAME, 'r').send_keys('1')
    # page_step.find_element(By.NAME, 's').send_keys('1')
    # page_step.find_element(By.NAME, 't').send_keys('1')



    #page_step.find_element(By.CSS_SELECTOR , "button[type='submit']").click()


    #select = Select(driver.find_element(By.NAME, 'g'))
    #select.select_by_visible_text('Bce')
    
    
    #from selenium.webdriver.support.ui import Select

    #select = Select(driver.find_element_by_id('fruits01'))

    #select.select_by_visible_text('Banana')

    #print (page_step.page_source)
