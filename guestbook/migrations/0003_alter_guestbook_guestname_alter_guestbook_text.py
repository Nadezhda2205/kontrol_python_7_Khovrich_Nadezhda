# Generated by Django 4.1.1 on 2022-10-01 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0002_rename_name_guestbook_guestname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestbook',
            name='guestname',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='guestbook',
            name='text',
            field=models.TextField(max_length=2000, verbose_name='Текст'),
        ),
    ]
