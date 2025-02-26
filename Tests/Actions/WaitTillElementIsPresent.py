from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def wiat_for_element(driver, xpath, timeout):
    try:
        element =WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )

    except TimeoutException:
        raise Exception(f"Element with XPath '{xpath}' was present {timeout} seconds.")

    element.is_displayed();