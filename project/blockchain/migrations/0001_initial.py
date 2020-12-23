# Generated by Django 3.0.3 on 2020-10-09 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(auto_created=True, blank=True)),
                ('time_stamp', models.DateTimeField()),
                ('data', models.TextField(blank=True, max_length=255)),
                ('hash', models.CharField(blank=True, max_length=255)),
                ('previous_hash', models.CharField(max_length=255)),
                ('nonce', models.CharField(blank=True, default=0, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(auto_created=True, blank=True, null=True)),
                ('product_id', models.IntegerField()),
                ('current_date', models.DateTimeField(auto_now=True)),
                ('expire_date', models.DateTimeField(blank=True)),
                ('country', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('common_name', models.TextField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]