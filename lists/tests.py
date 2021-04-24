#========================================
#lists/tests.py file
#Created by Plinio 04/23/2021
#Test Driven development book Chapter 3
#========================================

# internal function to resolve URLS and find what view function they should map to
#from django.urls import resolve #DELETE
from django.test import TestCase
#from django.http import HttpRequest #DELETE
#from django.template.loader import render_to_string #DELETE

#from lists.views import home_page #DELETE




class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get('/')
        print('>>> RESPONSE: ', response)
        self.assertTemplateUsed(response, 'home.html')

    #    def test_root_url_resolves_to_home_page_view(self):
#        found = resolve('/')
#        self.assertEqual(found.func,home_page)


#    def test_home_page_returns_correct_html(self):
        #request = HttpRequest()
        #response = home_page(request)
#        response = self.client.get('/')
#        html = response.content.decode('utf8')
#        self.assertTrue(html.startswith('<html>'))
#        self.assertIn('<title>To-Do lists</title>',html)
#        self.assertTrue(html.strip().endswith('</html>'))

#        self.assertTemplateUsed(response, 'wrong.html')
