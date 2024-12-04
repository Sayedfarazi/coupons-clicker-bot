import json
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import sys
import ssl
import certifi


ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())


def configure_chrome_options():
    """
    Set up Chrome options
    """
    options = Options()
    options.add_argument("disable-infobars")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("start-maximized")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--user-data-dir=chrome_data')  
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    )
    return options


def login_to_bjs(driver, email, password):
    """
    Log in to the BJ's website with the provided email and password from the secrets.json file. If login fails, print the error message and exit.
    """
    try:
        driver.get("https://www.bjs.com/signIn")
        print("Navigated to BJ's login page.")

        # Wait for the email input field
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "emailLogin"))
        )

        emailLogin = driver.find_element(By.ID, 'emailLogin')
        for character in email:
            emailLogin.send_keys(character)
            time.sleep(0.1)

        inputPassword = driver.find_element(By.ID, 'inputPassword')
        for character in password:
            inputPassword.send_keys(character)
            time.sleep(0.1)

        driver.find_element(By.XPATH, "//button[contains(@class, 'sign-in-submit-btn')]").click()
        print("Sign-In button clicked.")
        time.sleep(5)

        # Check for login success
        try:
            # Wait for a successful login indicator
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "signedInDrop"))
            )
            print("Login successful!")
        except Exception:
            # Check for login error message
            try:
                login_error_element = driver.find_element(By.XPATH, "//div[contains(@class, 'errMsgsignIn')]")
                print("Login failed:", login_error_element.text)
                sys.exit(1)
            except Exception:
                print("Unexpected login failure with no error message.")
                sys.exit(1)

    except Exception as e:
        print(f"An error occurred during login: {e}")
        sys.exit(1)


def clip_coupons(driver):
    """
    Go to the coupons page and click on all available coupons.
    """
    try:
        driver.get("https://www.bjs.com/myCoupons?source=header")
        print("Opened the coupons page.")
        time.sleep(5)

        # Find all the coupons
        coupons = driver.find_elements(By.XPATH, "//button[@name='clipToCard']")
        if not coupons:
            print("No coupons available to clip.")
            return

        print(f"Found {len(coupons)} coupons.")

        for idx, coupon in enumerate(coupons, 1):
            try:
                coupon.click()
                print(f"Clipped coupon {idx}.")
                time.sleep(1) 
            except Exception as e:
                print(f"Couldn't clip coupon {idx}: {e}")

    except Exception as e:
        print(f"Something went wrong on the coupons page: {e}")


def load_secrets(file_path="secrets.json"):
    """
    Read email and password from the JSON file.
    """
    try:
        with open(file_path, "r") as file:
            secrets = json.load(file)
            return secrets["email"], secrets["pass"]
    except FileNotFoundError:
        print(f"Secrets file '{file_path}' not found.")
        sys.exit(1)
    except KeyError as e:
        print(f"Missing key in secrets file: {e}")
        sys.exit(1)


def clicks(email, password):
    """
    Handle the main flow: log in to BJ's, then clip coupons.
    """
    options = configure_chrome_options()
    driver = uc.Chrome(options=options)

    try:
        login_to_bjs(driver, email, password)
        clip_coupons(driver)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        driver.quit()
        print("Process completed and browser closed.")


if __name__ == "__main__":
    bjs_email, bjs_password = load_secrets()
    clicks(bjs_email, bjs_password)
