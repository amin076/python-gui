# Generated by Django 2.2.2 on 2019-07-03 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc_app', '0002_auto_20190702_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='rectangle',
            name='date_recorded',
            field=models.DateField(auto_now=True),
        ),
    ]
