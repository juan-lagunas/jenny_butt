# Generated by Django 4.2.1 on 2023-05-10 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='part',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='log',
            old_name='part',
            new_name='name',
        ),
    ]
