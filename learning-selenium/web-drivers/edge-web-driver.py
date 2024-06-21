from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

driver.get("https://www.python.org/")
driver.maximize_window()

print(driver.title)

driver.close()