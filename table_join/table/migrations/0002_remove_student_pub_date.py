# Generated by Django 2.2.1 on 2019-11-16 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='pub_date',
        ),
    ]
