# Generated by Django 2.1.1 on 2018-09-08 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_time', models.DateTimeField()),
                ('request_ip', models.CharField(max_length=200)),
                ('machine_ip', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=254)),
            ],
        ),
    ]