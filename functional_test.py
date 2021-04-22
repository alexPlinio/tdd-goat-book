
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Check out user homepage
        self.browser.get('http://localhost:8000')
        #Check page title and header mention to-do list
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the Test!')

#The line below is used by python to run the script directly
#but not run it if the file is imported.
if __name__ == '__main__':
    #It then imports this modules, examines it, gets a list of all classes and functions which could
    #be tests (according the configuration) and then creates a test case for each of them.
    unittest.main(warnings='ignore')









#browser = webdriver.Firefox()
#browser.get('http://localhost:8000')
#assert 'To-Do' in browser.title, "Browser title was " + browser.title
#browser.quit()
