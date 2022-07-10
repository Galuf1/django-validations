# Generated by Django 4.0.6 on 2022-07-10 15:23

from django.db import migrations, models
import swimrecords.validator


class Migration(migrations.Migration):

    dependencies = [
        ('swimrecords', '0004_alter_swimrecord_distance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='swimrecord',
            name='record_date',
            field=models.DateTimeField(validators=[swimrecords.validator.validate_date]),
        ),
    ]