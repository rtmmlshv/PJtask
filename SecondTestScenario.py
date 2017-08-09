import unittest
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from ddt import ddt, data


@ddt
class MyTestCase(unittest.TestCase):

    @data ("http://github.com/","https://github.com/", "https://www.github.com/",
           "https://www.github.com/test/", "https://github.com/testlololo", "https://github.com/test?lol")
    def test_some(self, url):
        r = requests.head(url)
        print(r.status_code)
        if r.status_code == 200 :
            self.driver = webdriver.Firefox()
            self.driver.implicitly_wait(10)
            self.driver.get(url)
            try :
                print self.driver.title
                print self.driver.find_element_by_xpath("//meta[@name='description']").get_attribute("content")
                print self.driver.find_element_by_xpath("//h1").text
            except NoSuchElementException :
                print "Element not found"

            self.driver.quit()


if __name__ == '__main__':
    unittest.main()
