from guestbook.models import Guestbook
from django.forms import ModelForm

# class ProductForm(forms.Form):
#     name = forms.CharField(max_length=100, required=True, label='Наименование')
#     description = forms.CharField(widget=forms.Textarea, max_length=2000, required=False, label='Описание')
#     photo = forms.CharField(widget=forms.Textarea, max_length=2000, required=False, label='Фото')
#     category = forms.ChoiceField(choices=Product.CATEGORY_CHOICES, required=True, label='Категория',)
#     balance = forms.IntegerField(min_value=0, label='Остаток')
#     price = forms.DecimalField(max_digits=7, decimal_places=2, label='Стоимость')


class GuestbookForm(ModelForm):
    class Meta:
        model = Guestbook
        fields = ['guestname', 'mail', 'text']