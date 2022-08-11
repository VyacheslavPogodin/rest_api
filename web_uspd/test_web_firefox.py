
from time import sleep
from selenium import webdriver


from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



# Класс WebDriver добавлена функция пом=иска элемента с обработкой исключения NoSuchElementException и передачей в assert Pytest
class FindElementWithExcept(webdriver.Firefox):

    def find_element_with_exeption(self, metod, name):
        try: 
            element = driver.find_element(metod, name)
            return element
        except NoSuchElementException:
            assert False , f"На странице "+ driver.current_url +" не найден элемент: " + name

    def autenification(self, url, metod): #Аутентификация на сайте
        
        self.url = url
        self.metod = metod
        
        metod.get(url)
        metod.find_element_with_exeption(By.NAME, 'login').send_keys(login)
        metod.find_element_with_exeption(By.NAME, 'password').send_keys(password)
        metod.find_element_with_exeption(By.TAG_NAME, 'button').click()

        return metod


url = 'http://10.10.29.110/login'
login = 'user_admin'
password = 'admin123'


options = webdriver.FirefoxOptions()
#options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--headless")

#driver = webdriver.Firefox(service = Service(GeckoDriverManager().install()), options=options)
#driver.implicitly_wait(10)

driver = FindElementWithExcept(service = Service(GeckoDriverManager().install()), options=options)
driver.implicitly_wait(10)








# ТЕстовые классы

class TestWeb():

    def test_page_uspd_config(self):  # Проверяем наличие названия пунктов записей на странице

        driver.autenification(url, driver)
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
            assert name in  driver.page_source, "На странице "+ driver.current_url +f"отсутствует пункт с наименованием {name} отсуствует"
        

    def test_add_dev(self): # Добавляем новое устройство и проверяем что оно появилось в списке

        list_config = (
            'AUTOTEST',
            '123456789',
            '123456789ABCDEF0',
            '11',
            '21',
            '31',
        )

        driver.autenification(url, driver)
        sleep(3)
        driver.find_element_with_exeption(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div[3]/ul/li[1]').click()
        class_conf = 'MuiSwitch-switchBase MuiSwitch-colorPrimary MuiButtonBase-root MuiSwitch-switchBase MuiSwitch-colorPrimary PrivateSwitchBase-root css-svzrxe'
        if driver.find_element_with_exeption(By.XPATH, '//*[@id="simple-tabpanel-0"]/div/div[1]/table/div/div/span/span[1]').get_attribute('class') == class_conf:
            driver.find_element_with_exeption(By.XPATH, '//*[@id="simple-tabpanel-0"]/div/div[1]/table/div/div/span/span[1]/input').click()
        driver.find_element_with_exeption(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div[2]/ul/li[2]').click()
        driver.find_element_with_exeption(By.XPATH, '//*[@id="root"]/div[2]/main/div[2]/div/div[1]/button').click()
        driver.find_element_with_exeption(By.XPATH, '//*[@id="root"]/div[2]/main/div[2]/fieldset/div/label[1]/span[1]/input').click()
        
        #driver.get('http://10.10.29.110/devices/add')

        driver.find_element_with_exeption(By.NAME, 'a').send_keys('AUTOTEST')
        
        driver.find_element_with_exeption(By.NAME, 'b').click()
        driver.find_element_with_exeption(By.NAME, 'b').send_keys(Keys.ARROW_DOWN * 4 + Keys.ENTER)
        driver.find_element_with_exeption(By.NAME, 'b').click()
        
        driver.find_element_with_exeption(By.NAME, 'c').send_keys('123456789')
        driver.find_element_with_exeption(By.NAME, 'd').send_keys('123456789ABCDEF0')
        
        driver.find_element_with_exeption(By.NAME, 'h').click()
        driver.find_element_with_exeption(By.NAME, 'j').click()
        driver.find_element_with_exeption(By.NAME, 'k').click()
        driver.find_element_with_exeption(By.NAME, 'l').click()
        driver.find_element_with_exeption(By.NAME, 'm').click()

        # driver.find_element_with_exeption(By.NAME, 'g').click()
        # driver.find_element_with_exeption(By.NAME, 'g').send_keys(Keys.ARROW_DOWN + Keys.ENTER)
        # driver.find_element_with_exeption(By.NAME, 'g').click()

        driver.find_element_with_exeption(By.NAME, 'r').send_keys('11')
        driver.find_element_with_exeption(By.NAME, 's').send_keys('21')
        driver.find_element_with_exeption(By.NAME, 't').send_keys('31')
        driver.find_element_with_exeption(By.CSS_SELECTOR , "button[type='submit']").click()

        sleep(3)
        
        assert driver.current_url == 'http://10.10.29.110/devices', "После создания устройства, нет перехода на страницу http://10.10.29.110/devices"
        for conf in list_config:
            assert conf in driver.page_source, "На странице "+ driver.current_url + f" отсутствует параметр {conf}" 




if __name__ == '__main__':


    driver.autenification(url, driver)
    sleep(3)

    driver.find_element_with_exeption(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div[3]/ul/li[1]').click()
