from django.shortcuts import render
from guestbook.models import Guestbook

def guestsbook_view(request):
    guests = Guestbook.objects.all()
    context = {
        'guests': guests
    }
    return render(request=request, template_name='guests.html', context=context)

