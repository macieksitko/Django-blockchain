# Generated by Django 3.1.4 on 2021-01-03 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201227_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nonce',
            field=models.IntegerField(default=4836179),
        ),
    ]
