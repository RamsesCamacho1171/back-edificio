# Generated by Django 4.0.6 on 2023-08-13 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0001_initial'),
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='tenant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tenant.tenant'),
        ),
    ]
