# Generated by Django 4.2.1 on 2023-05-10 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_rename_categories_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='name',
            name='price',
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.name')),
            ],
        ),
    ]
