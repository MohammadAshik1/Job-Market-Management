from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/signup/")
driver.maximize_window()

test_cases = [
    {"name": "John Doe", "email": "john.doe@example.com", "password": "ValidPass123", "confirm_password": "ValidPass123", "expected": "success"},
    {"name": "", "email": "", "password": "", "confirm_password": "", "expected": "all_fields_required"},
    {"name": "", "email": "user@example.com", "password": "ValidPass123", "confirm_password": "ValidPass123", "expected": "name_required"},
    {"name": "John Doe", "email": "", "password": "ValidPass123", "confirm_password": "ValidPass123", "expected": "email_required"},
    {"name": "John Doe", "email": "invalid-email", "password": "ValidPass123", "confirm_password": "ValidPass123", "expected": "invalid_email_format"},
    {"name": "John Doe", "email": "user@example.com", "password": "", "confirm_password": "", "expected": "password_required"},
    {"name": "John Doe", "email": "user@example.com", "password": "Pass123", "confirm_password": "pass123", "expected": "password_mismatch"},
    {"name": "John123", "email": "user@example.com", "password": "ValidPass123", "confirm_password": "ValidPass123", "expected": "invalid_name_format"},
    {"name": "John Doe", "email": "already.registered@example.com", "password": "ValidPass123", "confirm_password": "ValidPass123", "expected": "duplicate_email"},
]

def test_registration(name, email, password, confirm_password, expected):
    try:
        name_field = driver.find_element(By.NAME, "username")
        email_field = driver.find_element(By.NAME, "email") 
        password_field = driver.find_element(By.NAME, "password") 
        confirm_password_field = driver.find_element(By.NAME, "re_password") 
        register_button = driver.find_element(By.XPATH, "//button[text()='Register']") 

        name_field.clear()
        email_field.clear()
        password_field.clear()
        confirm_password_field.clear()
        name_field.send_keys(name)
        email_field.send_keys(email)
        password_field.send_keys(password)
        confirm_password_field.send_keys(confirm_password)
        register_button.click()
        time.sleep(5)

        if expected == "success":
            assert "Welcome" in driver.page_source, "Registration failed for valid inputs!"
        else:
            error_message = driver.find_element(By.ID, "error-message").text
            assert error_message, f"No error message displayed for {expected}!"

        print(f"Test passed for: {email}")
    except AssertionError as e:
        print(f"Test failed for: {email} - {str(e)}")
    except Exception as ex:
        print(f"An error occurred: {str(ex)}")

for case in test_cases:
    test_registration(case["name"], case["email"], case["password"], case["confirm_password"], case["expected"])

driver.quit()
