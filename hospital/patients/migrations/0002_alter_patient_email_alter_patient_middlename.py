# Generated by Django 4.1.3 on 2022-11-23 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='patient',
            name='middlename',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
