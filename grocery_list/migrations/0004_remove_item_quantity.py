# Generated by Django 2.2 on 2019-04-27 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0003_auto_20190427_0831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='quantity',
        ),
    ]
