# Generated by Django 3.2.8 on 2021-10-24 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Download',
            new_name='Product',
        ),
        migrations.DeleteModel(
            name='Hotspot',
        ),
        migrations.DeleteModel(
            name='SDCard',
        ),
    ]
