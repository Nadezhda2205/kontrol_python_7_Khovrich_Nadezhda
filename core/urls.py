from django.contrib import admin
from django.urls import path
from guestbook.views import guestbooks_view, guestbooks_add_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', guestbooks_view, name='guestbooks'),
    path('guestbooks/add/', guestbooks_add_view, name='guestbooks_add'),
]
