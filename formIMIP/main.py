from selenium import  webdriver
import os
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

class bot:

    def inicio(self):
        self.data = input('Data: ')
        self.hora = input('Hora inicio: ')
        self.minuto = input('Minuto inicio: ')
        self.hora_fim = input('Hora fim: ')
        self.minuto_fim = input('Minuto fim: ')
        print('ANTÔNIO [1]')
        print('PELÁGIO [2]')
        print('ONLINE [3]')
        self.op_auditorio = int(input())
        self.nome_reuniao = input('Reunião')
        chrome_options = Options()
        chrome_options.add_argument('--window-size=1360,768')
        caminho_chromedriver = os.getcwd() + os.sep + 'chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=caminho_chromedriver, options=chrome_options)
        url = "https://docs.google.com/forms/d/e/1FAIpQLSdvCU9b852i8hrQt1C8E0UpqXf2Lw43wH_Mvm7am17Aiw2KiA/viewform?usp=pp_url&entry.1610534086=Teleeduca%C3%A7%C3%A3o&entry.1667369196=Reuni%C3%A3o&entry.596442700=Sim&entry.1162123463=N%C3%A3o&entry.809978340=8&entry.1359176809=Humberto"
        self.driver.get(url)
        time.sleep(3)

    def digitar_data(self):
        data = self.driver.find_element_by_xpath('//input[@class="quantumWizTextinputPaperinputInput exportInput"]')
        data.send_keys(self.data)

    def digitar_horario(self):
        horario = self.driver.find_elements_by_xpath('//input[@class="quantumWizTextinputPaperinputInput exportInput"]')
        horario[1].send_keys(self.hora)
        horario[2].send_keys(self.minuto)
        horario[3].send_keys(self.hora_fim)
        horario[4].send_keys(self.minuto_fim)

    def escolher_auditorio(self):
        if self.op_auditorio == 1:
            auditorio = self.driver.find_element_by_xpath('//div[@id="i15"]')
            auditorio.click()
        elif self.op_auditorio == 2:
            auditorio = self.driver.find_element_by_xpath('//div[@id="i18"]')
            auditorio.click()
        elif self.op_auditorio == 3:
            auditorio = self.driver.find_element_by_xpath('//div[@id="i33"]')
            auditorio.click()

        time.sleep(7)
        self.driver.find_element_by_xpath('//div[@class="appsMaterialWizButtonEl appsMaterialWizButtonPaperbuttonEl appsMaterialWizButtonPaperbuttonProtected freebirdFormviewerViewNavigationNoSubmitButton freebirdThemedProtectedButtonM2"]').click()


bot = bot()
bot.inicio()
bot.digitar_data()
bot.digitar_horario()
bot.escolher_auditorio()
