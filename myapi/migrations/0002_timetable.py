# Generated by Django 4.0.3 on 2022-03-25 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.DateTimeField()),
                ('type', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=12)),
                ('description', models.CharField(max_length=100)),
                ('staff', models.CharField(max_length=25)),
            ],
        ),
    ]
