# Generated by Django 4.0.3 on 2022-05-27 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_lab'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='l_no',
            field=models.IntegerField(null=True),
        ),
    ]