# Generated by Django 4.2.1 on 2023-05-11 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0024_alter_part_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
