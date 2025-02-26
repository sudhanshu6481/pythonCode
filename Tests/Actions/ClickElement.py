from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

SHORT_TIMEOUT = 10  # Default timeout for waits


def highlight_element(driver, element):
    driver.execute_script("arguments[0].style.border='3px solid yellow'", element)


def click_element(driver, xpath, timeout=SHORT_TIMEOUT):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )

        # Highlight the element
        highlight_element(driver, element)

        # Click the element
        element.click()

    except TimeoutException:
        raise Exception(f"Element with XPath '{xpath}' was not clickable within {timeout} seconds.")
