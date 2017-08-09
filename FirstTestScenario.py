import unittest
import time
from selenium import webdriver

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://the-internet.herokuapp.com/")

    def test_some(self):
        self.form_auth = self.driver.find_element_by_xpath("//a[text()='Form Authentication']")
        self.form_auth.click()
        self.userName_field = self.driver.find_element_by_id("username")
        self.userName_field.send_keys("tomsmith")
        self.pass_field = self.driver.find_element_by_id("password")
        self.pass_field.send_keys("SuperSecretPassword!")
        self.login_button = self.driver.find_element_by_xpath("//*[@id='login']/button")
        self.login_button.click()

        self.secure_header = self.driver.find_element_by_xpath("//*[@id='content']/div/h4")
        success_text = self.secure_header.text[:-134]
        asserting_text = "This is where you can log into the secure area."
        self.assertEqual(success_text, asserting_text)
        time.sleep(3)
        self.driver.save_screenshot("success_login.png")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
