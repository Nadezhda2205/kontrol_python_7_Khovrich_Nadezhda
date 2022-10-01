from django.shortcuts import render
from guestbook.models import Guestbook

def guestbooks_view(request):
    guestbooks = Guestbook.objects.all()
    context = {
        'guestbooks': guestbooks
    }
    return render(request=request, template_name='guestbooks.html', context=context)

