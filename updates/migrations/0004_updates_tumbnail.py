# Generated by Django 3.2.8 on 2022-02-10 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0003_auto_20220209_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='updates',
            name='Tumbnail',
            field=models.ImageField(default=1, upload_to='media/tour/tubnail'),
            preserve_default=False,
        ),
    ]
