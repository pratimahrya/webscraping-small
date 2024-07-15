from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Set up the Chrome WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Define the website URL
website = "https://www.adamchoi.co.uk/teamgoals/detailed"

# Open the website using the WebDriver
driver.get(website)
driver.maximize_window()

all_matches_button = driver.find_element(By.XPATH,'//label[@analytics-event="All matches"]')
all_matches_button.click()

matches = driver.find_elements(By.TAG_NAME, "tr")

date = []
home_team = []
score = []
away_team = []



for match in matches:
    print(match.text)


time.sleep(10)







driver.quit()
