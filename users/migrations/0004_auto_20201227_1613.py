# Generated by Django 3.0.3 on 2020-12-27 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201227_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='nonce',
            field=models.IntegerField(default=7701061),
        ),
    ]