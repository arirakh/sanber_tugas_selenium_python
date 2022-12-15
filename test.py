import unittest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


class SauceDemoLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    # 1
    def test_is_website_is_accessible(self):
      driver = self.driver
      driver.get("https://www.saucedemo.com/")

      self.assertIn("Swag", driver.title)

    # 2
    def test_login_with_empty_username_and_empty_password(self):
      driver = self.driver
      driver.get("https://www.saucedemo.com/")

      inputUsername = driver.find_element(By.NAME, "user-name")
      inputUsername.clear()
      inputUsername.send_keys("")

      inputPassword = driver.find_element(By.NAME, "password")
      inputPassword.clear()
      inputPassword.send_keys("")

      loginButton = driver.find_element(By.NAME, "login-button")
      loginButton.submit() 

      self.assertIn("Username is required", driver.page_source)

    # 3
    def test_login_with_filled_username_and_empty_password(self):
      driver = self.driver
      driver.get("https://www.saucedemo.com/")

      inputUsername = driver.find_element(By.NAME, "user-name")
      inputUsername.clear()
      inputUsername.send_keys("standard_user")

      inputPassword = driver.find_element(By.NAME, "password")
      inputPassword.clear()
      inputPassword.send_keys("")

      loginButton = driver.find_element(By.NAME, "login-button")
      loginButton.submit() 

      self.assertIn("Password is required", driver.page_source)
    
    # 4
    def test_login_with_right_username_and_wrong_password(self):
      driver = self.driver
      driver.get("https://www.saucedemo.com/")

      inputUsername = driver.find_element(By.NAME, "user-name")
      inputUsername.clear()
      inputUsername.send_keys("standard_user")

      inputPassword = driver.find_element(By.NAME, "password")
      inputPassword.clear()
      inputPassword.send_keys("secret_sauce123")

      loginButton = driver.find_element(By.NAME, "login-button")
      loginButton.submit() 

      self.assertIn("Username and password do not match any user in this service", driver.page_source)

    # 5
    def test_login_with_locked_out_user(self):
      driver = self.driver
      driver.get("https://www.saucedemo.com/")

      inputUsername = driver.find_element(By.NAME, "user-name")
      inputUsername.clear()
      inputUsername.send_keys("locked_out_user")

      inputPassword = driver.find_element(By.NAME, "password")
      inputPassword.clear()
      inputPassword.send_keys("secret_sauce")

      loginButton = driver.find_element(By.NAME, "login-button")
      loginButton.submit() 

      self.assertIn("Sorry, this user has been locked out.", driver.page_source)
      
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
