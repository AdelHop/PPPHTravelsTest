from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://www.kurs-selenium.pl/demo/")
driver.find_element("xpath","//span[text()='Search by Hotel or City Name']").click()
driver.find_element("xpath","//div[@id='select2-drop']//input").send_keys('Dubai')
driver.find_element("xpath","//span[text()='Dubai']").click()


time.sleep(100)

