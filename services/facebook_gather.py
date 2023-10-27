from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from app.parameters import FACEBOOKURL, EMAIL, FACEBOOKPASS
import time

class FacebookApi:
    url = FACEBOOKURL
    email = EMAIL
    senha = FACEBOOKPASS

    @property
    def checkText(self) -> str:

        options = webdriver.EdgeOptions()
        options.add_argument("headless")

        navegador = webdriver.Edge(options = options)

        navegador.get(self.url)

        elements = navegador.find_element(By.ID, "email").send_keys(self.email)
        elements = navegador.find_element(By.ID, "pass").send_keys(self.senha)
        elements = navegador.find_element(By.ID, "loginbutton").click()

        time.sleep(1)
        elements = navegador.find_elements(By.CSS_SELECTOR, 'div.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x1vvkbs')
        
        for element in elements:
            return element.text
        navegador.quit()
    
    @property
    def checkLocation(self) -> str:

        options = webdriver.EdgeOptions()
        options.add_argument("headless")

        navegador = webdriver.Edge(options = options)

        navegador.get(self.url)

        elements = navegador.find_element(By.ID, "email").send_keys(self.email)
        elements = navegador.find_element(By.ID, "pass").send_keys(self.senha)
        elements = navegador.find_element(By.ID, "loginbutton").click()

        time.sleep(1)
        elements = navegador.find_elements(By.CSS_SELECTOR, 'span.x193iq5w.xeuugli.x13faqbe.x1vvkbs.x1xmvt09.x1lliihq.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.xudqn12.x3x7a5m.x6prxxf.xvq8zen.xo1l8bm.xi81zsa.x1yc453h',)
        
        for element in elements:
            return element.text
        navegador.quit()