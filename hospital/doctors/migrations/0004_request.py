# Generated by Django 4.1.3 on 2022-11-27 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_appointmentdate_alter_doctor_schedule_details_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('contact_number', models.CharField(max_length=30)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.doctor')),
                ('timeslot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.appointmentdate')),
            ],
        ),
    ]