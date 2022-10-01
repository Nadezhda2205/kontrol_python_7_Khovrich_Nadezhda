from guestbook.models import Guestbook
from django.forms import ModelForm


class GuestbookForm(ModelForm):
    class Meta:
        model = Guestbook
        fields = ['guestname', 'mail', 'text']
