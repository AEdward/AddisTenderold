# Generated by Django 2.2.7 on 2020-01-15 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tenders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenders',
            name='Type',
        ),
        migrations.RemoveField(
            model_name='tenders',
            name='company_name',
        ),
    ]
