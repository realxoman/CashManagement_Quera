# Generated by Django 4.2.3 on 2023-07-16 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='balance',
            field=models.IntegerField(default=0, verbose_name='Balance'),
        ),
    ]
