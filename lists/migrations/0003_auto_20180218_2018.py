# Generated by Django 2.0rc1 on 2018-02-18 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_auto_20180218_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ship',
            name='type',
        ),
        migrations.AddField(
            model_name='ship',
            name='type',
            field=models.ManyToManyField(to='lists.Type'),
        ),
    ]
