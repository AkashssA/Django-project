# Generated by Django 5.1.1 on 2024-09-12 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
    ]
