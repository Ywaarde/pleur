# Generated by Django 3.1.5 on 2021-02-15 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('country', models.CharField(max_length=120)),
                ('website', models.CharField(max_length=120)),
            ],
        ),
    ]
