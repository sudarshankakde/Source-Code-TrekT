# Generated by Django 3.2.8 on 2022-02-10 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0005_auto_20220210_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=7)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('Phone_no1', models.IntegerField()),
                ('Phone_no2', models.IntegerField(blank=True, null=True)),
                ('address', models.TextField()),
                ('amount', models.IntegerField(default=0)),
                ('slotFor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='updates.updates')),
            ],
        ),
    ]
