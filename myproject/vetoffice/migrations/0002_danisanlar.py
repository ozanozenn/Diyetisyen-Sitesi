# Generated by Django 4.2.8 on 2024-01-04 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vetoffice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Danisanlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_soyad', models.CharField(max_length=100)),
                ('boy', models.FloatField()),
                ('kilo', models.FloatField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
