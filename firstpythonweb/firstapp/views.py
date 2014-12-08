from django.shortcuts import render_to_response
from firstapp.models import books
def index(request):
    booklist=books.objects.all()[:20]
    content={
        'bookid':1,
        'author':'amin',
        'title':'plastics'
    }
    return render_to_response('index.html',{'books':booklist})

