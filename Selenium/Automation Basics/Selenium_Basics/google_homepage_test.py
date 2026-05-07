from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=Service('../Resources/msedgedriver.exe'))
driver.get("https://www.google.com")
pagetitle = driver.title
if pagetitle == 'Google':
    print("Google Homepage Loaded - Pass")
else:
    print("Google Homepage NOT loaded - Fail")
driver.quit()