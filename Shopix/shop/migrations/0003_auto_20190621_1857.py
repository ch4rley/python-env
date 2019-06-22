# Generated by Django 2.2 on 2019-06-21 17:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190621_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(default=django.utils.timezone.now, unique=True, upload_to='upload/%Y/%m/%d'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
