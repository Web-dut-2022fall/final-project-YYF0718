# Generated by Django 2.2.1 on 2020-04-17 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200417_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='num',
            name='rates',
            field=models.FloatField(default=0, verbose_name='评分汇总'),
        ),
    ]
