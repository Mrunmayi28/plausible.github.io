# Generated by Django 3.1.7 on 2021-07-11 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210710_1940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modelaccept',
            old_name='name',
            new_name='fullname',
        ),
    ]
