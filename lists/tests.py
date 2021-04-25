#========================================
#lists/tests.py file
#Created by Plinio 04/23/2021
#Test Driven development book Chapter 3
#========================================

# internal function to resolve URLS and find what view function they should map to
#from django.urls import resolve #DELETE
from django.test import TestCase



class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data = {'item_text' : 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
