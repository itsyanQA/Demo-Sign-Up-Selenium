from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from techlistic_login_pom import TechlisticLogin

# Overall setup for the selenium, specifying the driver loaction, and the url to enter.
service_chrome = Service(r"C:\chromedriver.exe")
driver = webdriver.Chrome(service=service_chrome)
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
login = TechlisticLogin(driver)
driver.implicitly_wait(10)
driver.maximize_window()

# Press OK on the cookies section
while True:
    try:
        login.cookies_press_ok().click()
        break
    except:
        pass
# Enter first name
login.first_name().send_keys("yoyo")
# Enter last name
login.last_name().send_keys("jojo")
# Choose a gender from a dropdown list
login.choose_gender('Female').click()
# Choose years of experience - checkbox element
login.years_of_experience('5').click()
# Enter date
login.date_field('08/09/1999')
# Enter profession
login.profession('Automation Tester').click()
# Choose preferred automation tool
login.automation_tools('Selenium Webdriver').click()
# Choose continent from dropdown list
login.continents('Africa')
# Choose commands
login.commands('WebElement Commands')
# Upload profile picture
login.upload_image('C:\ProfilePicture.png')
# Download something in a new tab
login.download()
# Click the button
login.button().click()
# Quit 
driver.quit()


