# Generated by Django 4.2.3 on 2023-07-16 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='transaction_type',
            new_name='type',
        ),
    ]
