# Generated by Django 5.1 on 2024-08-15 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClimateData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('month', models.CharField(max_length=10)),
                ('value', models.FloatField()),
                ('parameter', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
            ],
            options={
                'unique_together': {('year', 'month', 'parameter', 'region')},
            },
        ),
    ]
