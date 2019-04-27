# Generated by Django 2.2 on 2019-04-27 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default='Produce', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grocerylist',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='grocery_list.Category'),
        ),
    ]