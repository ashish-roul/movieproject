# Generated by Django 3.1.5 on 2021-01-31 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reg',
            fields=[
                ('userid', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=25)),
                ('country', models.CharField(max_length=2)),
                ('pincode', models.IntegerField()),
                ('email', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=6)),
                ('language', models.CharField(max_length=2)),
                ('about', models.CharField(max_length=100)),
            ],
        ),
    ]
