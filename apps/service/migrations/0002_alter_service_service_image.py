# Generated by Django 3.2.25 on 2024-07-22 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service_image',
            field=models.ImageField(upload_to='services/'),
        ),
    ]