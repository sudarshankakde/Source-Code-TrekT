# Generated by Django 4.0.2 on 2022-07-02 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0021_rename_imageproduct_tourimages'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TourImages',
        ),
    ]
