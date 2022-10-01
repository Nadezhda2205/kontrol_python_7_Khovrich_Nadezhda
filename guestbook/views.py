from django.shortcuts import render, redirect
from guestbook.models import Guestbook
from django.core.handlers.wsgi import WSGIRequest
from guestbook.forms import GuestbookForm

def guestbooks_view(request):
    guestbooks = Guestbook.objects.order_by('-created_at').filter(status='active')
    context = {
        'guestbooks': guestbooks
    }
    return render(request=request, template_name='guestbooks.html', context=context)


def guestbooks_add_view(request:WSGIRequest):
    if request.method == 'POST':
        form = GuestbookForm(request.POST)
        if not form.is_valid():
            context = {
            'choices': Guestbook.CHOICES,
            'form': form
            }  
            return render(request=request, template_name='guestbooks.html', context=context)

        guestbook: Guestbook = Guestbook.objects.create(**form.cleaned_data)
        return redirect('guestbooks')

    form = GuestbookForm()
    context = {
        'choices': Guestbook.CHOICES,
        'form': form
    }    
    return render(request=request, template_name='guestbooks_add.html', context=context)


