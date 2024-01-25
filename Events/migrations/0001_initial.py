# Generated by Django 4.2.3 on 2023-11-30 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisteredUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('phone_number', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_date', models.DateTimeField(null=True)),
                ('end_date', models.DateTimeField(null=True)),
                ('registration_deadline', models.DateTimeField(null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('location', models.CharField(max_length=100, null=True)),
                ('center', models.CharField(max_length=100, null=True)),
                ('participant', models.ManyToManyField(blank=True, to='Events.registereduser')),
            ],
            options={
                'ordering': ['-end_date'],
            },
        ),
    ]
