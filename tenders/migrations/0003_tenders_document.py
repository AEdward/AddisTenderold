# Generated by Django 2.2.7 on 2020-12-08 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenders', '0002_remove_tenders_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenders',
            name='document',
            field=models.FileField(default='todo.txt', upload_to='media'),
        ),
    ]
