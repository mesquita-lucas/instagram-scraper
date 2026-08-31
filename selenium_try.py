from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USERNAME = "h4.tests"
PASSWORD = "Lululi3003!"

def configurar_driver():
    options = Options()
    options.add_experimental_option("detach", True)
    
    driver = webdriver.Chrome(options=options)
    
    return driver

driver = configurar_driver()
driver.get("https://instagram.com/hub4.bike")

def get_to_login(driver):
    wait = WebDriverWait(driver, 5)

    login_button = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[@role='button' and normalize-space()='Log in']"
            )
        )
    )

    login_button.click()

def login(driver):
    wait = WebDriverWait(driver, 5)

    username_input = wait.until(
            EC.visibility_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "input[name='email']"
                )
            )
        )

    password_input = wait.until(
                EC.visibility_of_element_located(
                    (
                        By.CSS_SELECTOR,
                        "input[name='pass']"
                    )
                )
            )

    username_input.send_keys(USERNAME)
    username_input.send_keys(PASSWORD)