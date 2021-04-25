
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

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
        
        #Location 1062 input
        header_text =  self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        #self.assertEqual(inputbox.get_attribute('placeholder'),
        #                'Enter a to-do item')
        #inputbox.send_keys('Buy peacock feathers')
        #inputbox.send_keys(Keys.ENTER)
        #time.sleep(1)

        #The page updates again...
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1:Buy peacock feathers',[row.text for row in rows])
        self.assertIn('2:Use peacock feathers to make a fly',[row.text for row in rows])

        self.fail('Finish The Test')
        

#The line below is used by python to run the script directly
#but not run it if the file is imported.
if __name__ == '__main__':
    #It then imports this modules, examines it, gets a list of all classes and functions which could
    #be tests (according the configuration) and then creates a test case for each of them.
    unittest.main(warnings='ignore')




