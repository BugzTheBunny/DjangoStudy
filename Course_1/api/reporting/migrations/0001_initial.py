# Generated by Django 5.1.3 on 2024-11-07 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('created_time', models.DateTimeField()),
            ],
        ),
    ]
