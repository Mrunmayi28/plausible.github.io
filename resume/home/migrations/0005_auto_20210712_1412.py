# Generated by Django 3.1.7 on 2021-07-12 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210712_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelaccept',
            name='awards',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='modelaccept',
            name='experience',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='modelaccept',
            name='skills',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
