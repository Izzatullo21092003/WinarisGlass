# Generated by Django 4.1.3 on 2022-11-21 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glass_shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benson',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
