#========================================
#lists/tests.py file
#Created by Plinio 04/23/2021
#Test Driven development book Chapter 3
#========================================

# internal function to resolve URLS and find what view function they should map to
#from django.urls import resolve #DELETE
from django.test import TestCase
from lists.models import Item


class ItemModelTest(TestCase):
    def test_saving_retrieving_items(self):
        first_item = Item()
        first_item.text = "The first (ever) list item"
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(),2)

        first_saved_item = saved_items[0]
        second_saved_item =saved_items[1]

        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')

class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

         
#    def test_redirects_after_POST(self):
#        response=self.client.post('/', data = {'item_text' : 'A new list item'})
#        self.assertEqual(response.status_code,302)
#        self.assertEqual(response['location'],
#                '/lists/the-only-list-in-the-world/')

    def home_page(request):
        if request.method == POST:
            new_item_text = request.POST['item_text']
            Item.objects.create(text = new_item_text)
        else:
            new_item_text=''
        return render(request, 'home.html', {
            'new_item_text':new_item_text,
            })
 #   def test_displays_all_list_items(self):
 #       Item.objects.create(text = 'itemey 1')
 #       Item.objects.create(text = 'itemey 2')
 #       response = self.client.get('/')
 #       self.assertIn('itemey 1', response.content.decode())
 #       self.assertIn('itemey 2', response.content.decode())

class ListViewTest(TestCase):    
    
    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'list.html')


    def test_displays_all_items(self):
        Item.objects.create(text = 'itemey 1')
        Item.objects.create(text = 'itemey 2')
            
        response = self.client.get('/lists/the-only-list-in-the-world/')
            
        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')

class NewListTest(TestCase):
    def test_can_save_a_POST_request(self):
        self.client.post('/lists/new', data = {'item_text' : 'A new list item'})
        self.assertEqual(Item.objects.count(),1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response=self.client.post('/lists/new', data = {'item_text' : 'A new list item'})
        #self.assertEqual(response.status_code,302)
        #self.assertEqual(response['location'],
        #        '/lists/the-only-list-in-the-world/')
        self.assertRedirects(response, '/lists/the-only-list-in-the-world/')

