# Generated by Django 3.2.25 on 2024-07-22 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_terms', models.CharField(choices=[('Monthly', 'Monthly'), ('Quarterly', 'Quarterly'), ('Annually', 'Annually')], max_length=100, null=True)),
                ('service_package', models.CharField(choices=[('Basic', 'Basic'), ('Standard', 'Standard'), ('Premium', 'Premium')], max_length=100, null=True)),
                ('service_name', models.CharField(choices=[('Web Development', 'Web Development'), ('Mobile Development', 'Mobile Development'), ('Cloud Services', 'Cloud Services'), ('Data Analytics', 'Data Analytics'), ('Cyber Security', 'Cyber Security'), ('Networking', 'Networking'), ('IT Support', 'IT Support'), ('AI & Machine Learning', 'AI & Machine Learning'), ('DevOps', 'DevOps'), ('Consulting', 'Consulting')], max_length=100, null=True)),
                ('service_price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('service_tax', models.DecimalField(decimal_places=2, max_digits=20, null=True)),
                ('service_image', models.ImageField(null=True, upload_to='services/')),
                ('active', models.BooleanField(default=True, null=True)),
            ],
        ),
    ]