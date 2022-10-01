from django.contrib import admin
from django.urls import path
from guestbook.views import guestbooks_view, guestbooks_add_view, guestbooks_edit_view, guestbooks_delete_view, confirm_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', guestbooks_view, name='guestbooks'),
    path('guestbooks/add/', guestbooks_add_view, name='guestbooks_add'),
    path('guestbooks/edit/<int:pk>', guestbooks_edit_view, name='guestbooks_edit'),
    path('guestbooks/delete/<int:pk>', guestbooks_delete_view, name='guestbooks_delete'),
    path('guestbooks/confirm/delete/<int:pk>', confirm_delete, name='confirm_delete'),
]
