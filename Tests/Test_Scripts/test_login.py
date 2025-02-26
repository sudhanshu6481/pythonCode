import pytest

import json

from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromiumService

from webdriver_manager.chrome import ChromeDriverManager

from webdriver_manager.core.os_manager import ChromeType

from selenium.common.exceptions import TimeoutException

from pytest_bdd import scenarios, given, when, then

import sys
import os

# Get the absolute path of the project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from Tests.Actions.ClickElement import click_element
from Tests.Actions.EnterText import enter_text
from Tests.Actions.WaitTillElementIsPresent import wiat_for_element
# Load the JSON file
try:
    with open('/home/sudhanshugupta/PycharmProjects/PythonProject/Tests/ObjectFactory/ObjectRepository.json', 'r') as file:
       data = json.load(file)
except json.JSONDecodeError as e:
    print(f"JSON decoding failed: {e}")

try:
    with open('/home/sudhanshugupta/PycharmProjects/PythonProject/Tests/env.json', 'r') as env:
       credentials = json.load(env)
except json.JSONDecodeError as e:
    print(f"JSON decoding failed: {e}")

scenarios('../Features/login.feature')

SHORT_TIMEOUT  = 10   # give enough time for the loading element to appear
LONG_TIMEOUT = 30  # give enough time for loading to finish

@pytest.fixture

def driver():

   browser = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

   yield browser

   browser.quit()

@given('the user is on the login page')

def navigate_to_login(driver):

   driver.get(credentials["base_url"])

   driver.maximize_window()

@when('the user enters valid credentials')

def enter_credentials(driver):

   #Enter username

   enter_text(driver,data["UserName"],credentials["username"])
   #driver.find_element(By.XPATH, data["UserName"]).send_keys(credentials["username"])

   click_element(driver,data["SubmitButton"])
   #driver.find_element(By.XPATH, data["SubmitButton"]).click()

   wiat_for_element(driver, data["Password"], SHORT_TIMEOUT)
   #WebDriverWait(driver, SHORT_TIMEOUT).until(EC.presence_of_element_located((By.XPATH, data["Password"])))

   #Enter password

   enter_text(driver, data["Password"], credentials["password"])
   #driver.find_element(By.XPATH,data["Password"]).send_keys(credentials["password"])

   #click submit

   click_element(driver,data["SubmitButton"])

   #wait for loader to disappear
   try:
      wiat_for_element(driver, data["LOADING_ELEMENT_XPATH"], SHORT_TIMEOUT)
      #WebDriverWait(driver, SHORT_TIMEOUT).until(EC.presence_of_element_located((By.XPATH, data["LOADING_ELEMENT_XPATH"])))

   except TimeoutException:
      pass

@then('the user should be logged in')

def verify_login(driver):

   wiat_for_element(driver, data["Logo"], SHORT_TIMEOUT)
   #WebDriverWait(driver, SHORT_TIMEOUT).until(EC.presence_of_element_located((By.XPATH, data["Logo"])))

   assert driver.title=="RightNow Track"