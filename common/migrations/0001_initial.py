# Generated by Django 2.0.7 on 2018-07-13 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MiscStorageEntry',
            fields=[
                ('key', models.CharField(db_index=True, max_length=64, primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=256)),
            ],
        ),
    ]
