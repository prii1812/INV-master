# Generated by Django 4.1.7 on 2023-04-30 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_issued_items_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='issued_items',
            name='is_accepted',
            field=models.BooleanField(default='False'),
        ),
    ]
