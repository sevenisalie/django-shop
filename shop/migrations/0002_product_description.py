# Generated by Django 3.1.1 on 2020-09-06 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
