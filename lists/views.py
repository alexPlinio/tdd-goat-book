#====================================
# lists/views.py
#====================================

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return render(request, 'home.html', {
        'new_item_text':request.POST.get('item_text'),
        })

#    if request.method == 'POST': #DELETE
#        return HttpResponse (request.POST['item_text']) #DELETE
#    return render(request,'home.html') #DELETE
    


