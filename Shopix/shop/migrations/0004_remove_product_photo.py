# Generated by Django 2.2 on 2019-06-21 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20190621_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='photo',
        ),
    ]
