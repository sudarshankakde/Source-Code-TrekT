# Generated by Django 4.0.2 on 2022-05-09 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0012_alter_contact_contact_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='updates',
            name='TourExpire',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
