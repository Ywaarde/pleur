# Generated by Django 3.1.5 on 2021-02-15 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roasters', '0001_initial'),
        ('coffees', '0003_delete_roaster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee',
            name='roaster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roasters.roaster'),
        ),
    ]
