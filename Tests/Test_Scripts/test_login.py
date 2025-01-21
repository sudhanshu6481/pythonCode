import pytest

import json

from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromiumService

from webdriver_manager.chrome import ChromeDriverManager

from webdriver_manager.core.os_manager import ChromeType

from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from selenium.common.exceptions import TimeoutException

from pytest_bdd import scenarios, given, when, then

# Load the JSON file
try:
    with open('/home/sudhanshugupta/PycharmProjects/PythonProject/Tests/ObjectFactory/ObjectRepository.json', 'r') as file:
       data = json.load(file)
except json.JSONDecodeError as e:
    print(f"JSON decoding failed: {e}")

scenarios('../Features/login.feature')

LOADING_ELEMENT_XPATH = data["LOADING_ELEMENT_XPATH"]
SHORT_TIMEOUT  = 10   # give enough time for the loading element to appear
LONG_TIMEOUT = 30  # give enough time for loading to finish

@pytest.fixture

def driver():

   browser = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

   yield browser

   browser.quit()

@given('the user is on the login page')

def navigate_to_login(driver):

   driver.get("https://qa-track.rightnowinventory.com/")

   #wait for loader to disappear
   try:
      WebDriverWait(driver, SHORT_TIMEOUT).until(EC.presence_of_element_located((By.XPATH, LOADING_ELEMENT_XPATH)))

   except TimeoutException:
      pass

@when('the user enters valid credentials')

def enter_credentials(driver):

   #Enter username

   driver.find_element(By.XPATH, data["UserName"]).send_keys("karate003.automation@gmail.com")

   driver.find_element(By.XPATH, data["SubmitButton"]).click()

   WebDriverWait(driver, SHORT_TIMEOUT).until(EC.presence_of_element_located((By.XPATH, data["Password"])))

   #Enter password

   driver.find_element(By.XPATH,data["Password"]).send_keys("Cloudsufi@123")

   #click submit

   driver.find_element(By.XPATH,data["SubmitButton"]).click()

   #wait for loader to disappear
   try:
      WebDriverWait(driver, SHORT_TIMEOUT).until(EC.presence_of_element_located((By.XPATH, data["LOADING_ELEMENT_XPATH"])))

   except TimeoutException:
      pass

@then('the user should be logged in')

def verify_login(driver):

   WebDriverWait(driver, SHORT_TIMEOUT).until(EC.presence_of_element_located((By.XPATH, data["Logo"])))

   assert driver.title=="RightNow Track"