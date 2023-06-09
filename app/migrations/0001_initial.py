# Generated by Django 4.2 on 2023-04-16 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.IntegerField(auto_created = True,verbose_name = 'ID', primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200)),
                ('DOB', models.DateField()),
                ('DOJ', models.DateField()),
                ('Department', models.CharField(max_length=200)),
                ('Post', models.CharField(max_length=200)),
                ('Address', models.TextField()),
                ('City', models.CharField(max_length=200)),
                ('Country', models.CharField(max_length=200)),
                ('Zipcode', models.IntegerField(max_length=200)),
                ('State', models.CharField(max_length=200)),
                ('Active', models.BooleanField(default=False)),
            ],
        ),
    ]
