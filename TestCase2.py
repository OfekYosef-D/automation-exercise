from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

def test_home_page():
    # 1. Launch browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    try:
        # 2. Navigate to url 'http://automationexercise.com'
        driver.get("http://automationexercise.com")

        # 3. Verify that home page is visible successfully
        slider = driver.find_element(By.ID, "slider")
        assert slider.is_displayed(), "Home page is not visible"

        # 4. Click on 'Signup / Login' button
        login_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Signup / Login")
        login_link.click()

        # 5. Verify 'New User Signup!' is visible
        check_title = driver.find_element(By.XPATH, "//*[text()='Login to your account']")
        assert check_title.is_displayed(), "New User Signup is not visible"

        # 6. Enter correct email address and password
        email_input = driver.find_element(By.CSS_SELECTOR, "[data-qa='login-email']")
        password_input = driver.find_element(By.CSS_SELECTOR, "[data-qa='login-password']")
        email_input.send_keys("noder@gmail.com")
        password_input.send_keys("s1h2a3r4")

        # 7. Click 'login' button
        login_button = driver.find_element(By.CSS_SELECTOR, "[data-qa='login-button']")
        login_button.click()

        # 8. Verify that 'Logged in as username' is visible
        check_title = driver.find_element(By.XPATH, "//a[contains(text(), 'Logged in as')]")
        assert check_title.is_displayed(), "Logged in as is not visible"

        # 9. Click 'Delete Account' button
        delete_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Delete Account")
        delete_button.click()

        # 10. Verify that 'ACCOUNT DELETED!' is visible
        check_title = driver.find_element(By.XPATH, "//*[text()='Account Deleted!']")
        assert check_title.is_displayed(), "Account deleting failed"

    finally:
        time.sleep(3)
        driver.quit()

if __name__ == "__main__":
    test_home_page()
