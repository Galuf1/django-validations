# Generated by Django 4.0.6 on 2022-07-10 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swimrecords', '0002_alter_swimrecord_stroke'),
    ]

    operations = [
        migrations.AlterField(
            model_name='swimrecord',
            name='relay',
            field=models.BooleanField(blank=False,null=False,default=True),
        ),
    ]