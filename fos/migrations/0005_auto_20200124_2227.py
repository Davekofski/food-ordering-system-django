# Generated by Django 3.0.2 on 2020-01-24 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fos', '0004_auto_20200124_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custorderstatus',
            name='delivery_person_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='delivery_person_id', to='fos.DeliveryPerson'),
        ),
    ]
