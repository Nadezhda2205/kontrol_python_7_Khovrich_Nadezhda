
from django.contrib import admin
from django.urls import path
from guestbook.views import guestsbook_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', guestsbook_view, name='guestsbook'),
]
