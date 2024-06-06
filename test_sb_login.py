import time  # for importing libraries for time
import os
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By  # by is the class in selenium so for this imported By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains  # library for performing mouse actions
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture()
def fixture_setup():
    headless = os.getenv('HEADLESS', 'false').lower() == 'true'
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options
    #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # give the version of chrome in install () here
    driver.get("https://saas-sbdt-dev-app-web-du-uae.azurewebsites.net/#/Login")  # hitting the url
    driver.maximize_window()  # for maximizing the window
    yield  # after yield what we will be writing will execute after testcase.
    driver.close()

# def scroll_to_element(element):
    # driver.execute_script("arguments[0].scrollIntoView(true);", element)

def test_sb_login(fixture_setup):
    wait = WebDriverWait(driver, 10)
    time.sleep(4)

    email = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/form/div[1]/input")))
    time.sleep(4)
    email.send_keys("mujtabaaziz@yopmail.com")
    time.sleep(4)

    password = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/form/div[2]/input")
    time.sleep(4)
    # scroll_to_element(password)  # scrolling to password field
    password.send_keys("Aa123456@")
    time.sleep(2)

    view_password_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "html > body > div:first-of-type > div > div > div:nth-of-type(2) > div > div > div > form > div:nth-of-type(2) > div > svg")))
    time.sleep(2)
    # scroll_to_element(view_password_button)
    ActionChains(driver).move_to_element(view_password_button).click().perform()  # for moving cursor to perform action
    time.sleep(2)

    # remember_me_checkbox = driver.find_element(By.ID, "id_remember_me")
    # if not remember_me_checkbox.is_selected():
        # remember_me_checkbox.click()

    login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/form/button")
    time.sleep(4)
    # scroll_to_element(login_button)
    ActionChains(driver).move_to_element(login_button).click().perform()  # for moving cursor to perform action
    time.sleep(4)

    select_building = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/section/div/div/div/div[3]/div/div/div/div/div/button")))
    time.sleep(2)
    ActionChains(driver).move_to_element(select_building).click().perform()
    time.sleep(3)

    # Scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    # Scroll back to the top of the page
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)

    # for navigating back to prevoius page.
    driver.back()
    time.sleep(3)

    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)

    logout_button = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/header/nav/div/div/div[3]/form/ul/li[2]/button")))
    time.sleep(3)
    # scroll_to_element(logout_button)
    ActionChains(driver).move_to_element(logout_button).click().perform()

    time.sleep(5)
    assert "SB DT Twin" in driver.title
