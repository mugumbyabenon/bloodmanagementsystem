# Generated by Django 3.2.18 on 2023-05-14 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='email',
            field=models.EmailField(default='legacyallan0@gmail.com', max_length=254),
        ),
    ]
