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
        check_title = driver.find_element(By.XPATH, "//*[text()='New User Signup!']")
        assert check_title.is_displayed(), "New User Signup is not visible"

        # 6. Enter name and email address
        name_input = driver.find_element(By.CSS_SELECTOR, "[data-qa='signup-name']")
        email_input = driver.find_element(By.CSS_SELECTOR, "[data-qa='signup-email']")
        name_input.send_keys("Yahav")
        email_input.send_keys("nodernedarim@gmail.com")

        # 7. Click 'Signup' button
        signup_button = driver.find_element(By.CSS_SELECTOR, "[data-qa='signup-button']")
        signup_button.send_keys(Keys.RETURN)

        # 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
        check_title = driver.find_element(By.XPATH, "//*[text()='Enter Account Information']")
        assert check_title.is_displayed(), "Account Information Page is not visible"

        # 9. Fill details: Title, Name, Email, Password, Date of birth
        gender_tickbox = driver.find_element(By.ID, "id_gender2").click()
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("s1h2a3r4o5n6")
        day_dropdown = Select(driver.find_element(By.ID, "days"))
        month_dropdown = Select(driver.find_element(By.ID, "months"))
        year_dropdown = Select(driver.find_element(By.ID, "years"))
        day_dropdown.select_by_value("19")
        month_dropdown.select_by_value("2")
        year_dropdown.select_by_value("2003")

        # 10. Select checkbox 'Sign up for our newsletter!'
        news_tickbox = driver.find_element(By.ID, "newsletter").click()

        # 11. Select checkbox 'Receive special offers from our partners!'
        offers_tickbox = driver.find_element(By.ID, "optin").click()

        # 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
        first_name_input = driver.find_element(By.ID, "first_name")
        last_name_input = driver.find_element(By.ID, "last_name")
        company_input = driver.find_element(By.ID, "company")
        address1_input = driver.find_element(By.ID, "address1")
        address2_input = driver.find_element(By.ID, "address2")
        country_dropdown = Select(driver.find_element(By.ID, "country"))
        state_input = driver.find_element(By.ID, "state")
        city_input = driver.find_element(By.ID, "city")
        zipcode_input = driver.find_element(By.ID, "zipcode")
        mobile_number_input = driver.find_element(By.ID, "mobile_number")
        
        # Inputting data after selecting each input / dragdown boxes
        first_name_input.send_keys("Yahav")
        last_name_input.send_keys("Yosef")
        company_input.send_keys("O&Y Forever")
        address1_input.send_keys("Tora Ve Avoda 26")
        address2_input.send_keys("Dori Yaakov 6")
        country_dropdown.select_by_value("Israel")
        state_input.send_keys("Israel")
        city_input.send_keys("Rishon LeTzion")
        zipcode_input.send_keys("7561813")
        mobile_number_input.send_keys("0533384993")


        # 13. Click 'Create Account button'
        create_account_button = driver.find_element(By.CSS_SELECTOR, "[data-qa='create-account']")
        create_account_button.click()

        # 14. Verify that 'ACCOUNT CREATED!' is visible
        check_title = driver.find_element(By.XPATH, "//*[text()='Account Created!']")
        assert check_title.is_displayed(), "Account creating failed."

        # 15. Click 'Continue' button
        continue_button = driver.find_element(By.CSS_SELECTOR, "[data-qa='continue-button']")
        continue_button.click()

        # 16. Verify that 'Logged in as username' is visible
        check_title = driver.find_element(By.XPATH, "//a[contains(text(), 'Logged in as')]")
        assert check_title.is_displayed(), "Logged in as Yahav is not visible"

        # 17. Click 'Delete Account' button
        delete_account_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Delete Account")
        delete_account_button.click()

        # 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
        check_title = driver.find_element(By.XPATH, "//*[text()='Account Deleted!']")
        assert check_title.is_displayed(), "Account deleting failed"

        continue_button = driver.find_element(By.CSS_SELECTOR, "[data-qa='continue-button']")
        continue_button.click()
    finally:
        time.sleep(3)
        driver.quit()

if __name__ == "__main__":
    test_home_page()
