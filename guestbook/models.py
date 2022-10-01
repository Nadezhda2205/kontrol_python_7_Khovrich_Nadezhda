from django.db import models

class Guestbook(models.Model):

    CHOICES = [
    ('active', 'Активно'),
    ('blocked', 'Заблокировано'),
]
    guestname = models.CharField(verbose_name='Имя', max_length=100, null=False, blank=False)
    mail = models.EmailField(verbose_name='Почта', null=False, blank=False)
    text = models.TextField(verbose_name='Текст', max_length=2000, null=False, blank=False)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)
    status = models.CharField(
        verbose_name='Активно', 
        max_length=15, 
        null=False, 
        blank=False, 
        default='active',
        choices=CHOICES)

    def __str__(self) -> str:
        return self.guestname