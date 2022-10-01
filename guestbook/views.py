from django.shortcuts import render, redirect, get_object_or_404
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


def guestbooks_edit_view(request, pk):
    if request.method == 'POST':
        guestbook = get_object_or_404(Guestbook, pk=pk)
        form = GuestbookForm(request.POST, instance=guestbook)
        if not form.is_valid():
            context = {
            'form': form
            }  
            return render(request=request, template_name='guestbooks_edit.html', context=context)

        form.save()
        return redirect('guestbooks')
        
    guestbook = get_object_or_404(Guestbook, pk=pk)
    form = GuestbookForm(instance=guestbook)
    context = {
        'form': form
    }
    return render(request=request, template_name='guestbooks_edit.html', context=context)


def guestbooks_delete_view(request, pk):
    guestbook = get_object_or_404(Guestbook, pk=pk)
    context = {
        'guestbook': guestbook
    }
    return render(request, 'confirm_delete.html', context)


def confirm_delete(request, pk):
    guestbook = get_object_or_404(Guestbook, pk=pk)
    guestbook.delete()
    return redirect('guestbooks')
