# Generated by Django 2.2 on 2019-06-21 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.ImageField(unique=True, upload_to='upload/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='image',
            name='position',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
