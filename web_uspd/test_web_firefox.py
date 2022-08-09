
from time import sleep
from selenium import webdriver
#from selenium.webdriver.firefox.webdriver import WebDriver

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
#from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#from selenium.webdriver.support.ui import Select



url = 'http://10.10.29.110/login'
login = 'user_admin'
password = 'admin123'
options = webdriver.FirefoxOptions()
#options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--headless")

driver = webdriver.Firefox(service = Service(GeckoDriverManager().install()), options=options)
driver.implicitly_wait(10)

def autenification(url, metod): #Аутентификация на сайте
    metod.get(url)
    find_element_with_exeption(metod ,By.NAME, 'login').send_keys(login)
    find_element_with_exeption(metod ,By.NAME, 'password').send_keys(password)
    find_element_with_exeption(metod ,By.TAG_NAME, 'button').click()
    return metod


def find_element_with_exeption(driver, metod, name):
    try: 
        element = driver.find_element(metod, name)
        return element
    except NoSuchElementException:
        assert False , f"На странице "+ driver.current_url +" не найден элемент: " + name



# ТЕстовые классы

class TestWeb():

    def test_page_uspd_config(self):  # Проверяем наличие названия пунктов записей на странице

        page_step = autenification(url, driver)
        sleep(4)

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
            assert name in  page_step.page_source, "На странице "+ page_step.current_url +f"отсутствует пункт с наименованием {name} отсуствует"
        

    def test_add_dev(self): # Добавляем новое устройство и проверяем что оно появилось в списке

        list_config = (
            'AUTOTEST',
            '123456789',
            '123456789ABCDEF0',
            '11',
            '21',
            '31',
        )

        page_step = autenification(url, driver)
        sleep(3)
        find_element_with_exeption(page_step ,By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div[3]/ul/li[1]').click()
        class_conf = 'MuiSwitch-switchBase MuiSwitch-colorPrimary MuiButtonBase-root MuiSwitch-switchBase MuiSwitch-colorPrimary PrivateSwitchBase-root css-svzrxe'
        if find_element_with_exeption(page_step ,By.XPATH, '//*[@id="simple-tabpanel-0"]/div/div[1]/table/div/div/span/span[1]').get_attribute('class') == class_conf:
            find_element_with_exeption(page_step ,By.XPATH, '//*[@id="simple-tabpanel-0"]/div/div[1]/table/div/div/span/span[1]/input').click()
        find_element_with_exeption(page_step ,By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div[2]/ul/li[2]').click()
        find_element_with_exeption(page_step ,By.XPATH, '//*[@id="root"]/div[2]/main/div[2]/div/div[1]/button').click()
        find_element_with_exeption(page_step ,By.XPATH, '//*[@id="root"]/div[2]/main/div[2]/fieldset/div/label[1]/span[1]/input').click()
        
        #page_step.get('http://10.10.29.110/devices/add')

        find_element_with_exeption(page_step ,By.NAME, 'a').send_keys('AUTOTEST')
        
        find_element_with_exeption(page_step ,By.NAME, 'b').click()
        find_element_with_exeption(page_step ,By.NAME, 'b').send_keys(Keys.ARROW_DOWN * 4 + Keys.ENTER)
        find_element_with_exeption(page_step ,By.NAME, 'b').click()
        
        find_element_with_exeption(page_step ,By.NAME, 'c').send_keys('123456789')
        find_element_with_exeption(page_step ,By.NAME, 'd').send_keys('123456789ABCDEF0')
        
        find_element_with_exeption(page_step ,By.NAME, 'h').click()
        find_element_with_exeption(page_step ,By.NAME, 'j').click()
        find_element_with_exeption(page_step ,By.NAME, 'k').click()
        find_element_with_exeption(page_step ,By.NAME, 'l').click()
        find_element_with_exeption(page_step ,By.NAME, 'm').click()

        # find_element_with_exeption(page_step ,By.NAME, 'g').click()
        # find_element_with_exeption(page_step ,By.NAME, 'g').send_keys(Keys.ARROW_DOWN + Keys.ENTER)
        # find_element_with_exeption(page_step ,By.NAME, 'g').click()

        find_element_with_exeption(page_step ,By.NAME, 'r').send_keys('11')
        find_element_with_exeption(page_step ,By.NAME, 's').send_keys('21')
        find_element_with_exeption(page_step ,By.NAME, 't').send_keys('31')
        find_element_with_exeption(page_step ,By.CSS_SELECTOR , "button[type='submit']").click()

        sleep(3)
        
        assert page_step.current_url == 'http://10.10.29.110/devices', "После создания устройства, нет перехода на страницу http://10.10.29.110/devices"
        for conf in list_config:
            assert conf in page_step.page_source, "На странице "+ page_step.current_url + f" отсутствует параметр {conf}" 




if __name__ == '__main__':


    page_step = autenification(url, driver)
    sleep(3)
    
    find_element_with_exeption(page_step ,By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div[3]/ul/li[0]').click()

    #select = Select(driver.find_element(By.NAME, 'g'))
    #select.select_by_visible_text('Bce')
    
    
    #from selenium.webdriver.support.ui import Select

    #select = Select(driver.find_element_by_id('fruits01'))

    #select.select_by_visible_text('Banana')

    #print (page_step.page_source)