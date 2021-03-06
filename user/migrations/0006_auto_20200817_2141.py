# Generated by Django 3.0.8 on 2020-08-17 16:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_sem4_sem5_sem6_sem7_sem8'),
    ]

    operations = [
        migrations.AddField(
            model_name='sem2',
            name='BasicElectricalElectronicsandInstrumentationEngineeringLaboratory',
            field=models.CharField(choices=[('O', 'O'), ('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('RA', 'Arrear')], default=django.utils.timezone.now, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='main',
            name='RegisterNumber',
            field=models.CharField(max_length=12, primary_key=True, serialize=False, unique=True),
        ),
    ]
