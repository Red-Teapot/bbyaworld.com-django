# Generated by Django 2.0.7 on 2018-07-16 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_nickname', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('label', models.CharField(max_length=128)),
                ('area', models.FloatField()),
            ],
        ),
    ]
