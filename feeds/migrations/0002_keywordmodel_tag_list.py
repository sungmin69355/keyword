# Generated by Django 3.1.4 on 2020-12-17 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='keywordmodel',
            name='tag_list',
            field=models.CharField(default='', max_length=400),
        ),
    ]