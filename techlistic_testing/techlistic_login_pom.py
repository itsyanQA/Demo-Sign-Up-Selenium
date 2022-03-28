from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class TechlisticLogin:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    def first_name(self):
        return self.driver.find_element(By.XPATH, "//div/input[@name='firstname']")

    def last_name(self):
        return self.driver.find_element(By.XPATH, "//div/input[@name='lastname']")

    def choose_gender(self, gender):
        genders = self.driver.find_elements(By.XPATH, "//div/input[@name='sex']")
        for i in genders:
            if i.get_attribute("value") == gender:
                return i
            else:
                pass

    def years_of_experience(self, selected_year):
        years = self.driver.find_elements(By.XPATH, '//div/input[@name="exp"]')
        for year in years:
            if year.get_attribute("value") == selected_year:
                return year
            else:
                pass

    def date_field(self, date):
        date_field = self.driver.find_element(By.ID, "datepicker")
        date_field.send_keys(date)

    def profession(self, selected_profession):
        professions = self.driver.find_elements(By.XPATH, '//div/input[@name="profession"]')
        for profession in professions:
            if selected_profession == profession.get_attribute("value"):
                return profession
            else:
                pass

    def automation_tools(self, selected_tool):
        tools = self.driver.find_elements(By.XPATH, '//div/input[@name="tool"]')
        for tool in tools:
            if tool.get_attribute("value") == selected_tool:
                return tool
            else:
                pass

    def continents(self, continent):
        continents = self.driver.find_element(By.ID, "continents")
        continents = Select(continents)
        continents.select_by_visible_text(continent)

    def cookies_press_ok(self):
        return self.driver.find_element(By.ID, 'cookieChoiceDismiss')

    def commands(self, command):
        commands = Select(self.driver.find_element(By.ID, "selenium_commands"))
        commands.select_by_visible_text(command)

    def upload_image(self, picture_path):
        upload = self.driver.find_element(By.ID, "photo")
        upload.send_keys(picture_path)

    def download(self):
        download = self.driver.find_element(By.LINK_TEXT, "Click here to Download File")
        self.action.context_click(download).send_keys(Keys.ENTER).perform()

    def button(self):
        return self.driver.find_element(By.CLASS_NAME, "btn-info")

