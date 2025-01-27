from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/login/")
driver.maximize_window()

test_cases = [
    {"username": "invalid_user", "password": "WrongPassword", "expected": "invalid"},
    {"username": "", "password": "", "expected": "required"},
    {"username": "", "password": "SomePassword", "expected": "username_required"},
    {"username": "XUser", "password": "", "expected": "password_required"},
    {"username": "user!@#", "password": "ValidPassword123", "expected": "invalid_username_format"},
    {"username": "Shaon", "password": "123", "expected": "password_too_short"},
    {"username": "Ashik", "password": "+123456-", "expected": "success"},
]

def test_login(username, password, expected):
    try:

        username_field = driver.find_element(By.NAME, "username") 
        password_field = driver.find_element(By.NAME, "password")  
        login_button = driver.find_element(By.XPATH, "//button[text()='Login']") 

       
        username_field.clear()
        password_field.clear()
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()
        time.sleep(5)

        if expected == "success":
            assert "Dashboard" in driver.title, "Login failed for valid credentials!"
        elif expected in ["invalid", "required", "username_required", "password_required"]:
            error_message = driver.find_element(By.ID, "error-message").text
            assert error_message, f"No error message displayed for {expected}!"
        elif expected == "prevent_sql_injection":
            error_message = driver.find_element(By.ID, "error-message").text 
            assert "Invalid credentials" in error_message, "SQL injection test failed!"

        print(f"Test passed for: {username}")
    except AssertionError as e:
        print(f"Test failed for: {username} - {str(e)}")
    except Exception as ex:
        print(f"An error occurred: {str(ex)}")

for case in test_cases:
    test_login(case["username"], case["password"], case["expected"])

driver.quit()
