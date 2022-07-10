# Generated by Django 4.0.6 on 2022-07-10 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SwimRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('team_name', models.CharField(max_length=50)),
                ('relay', models.BooleanField()),
                ('stroke', models.CharField(max_length=50)),
                ('distance', models.IntegerField()),
                ('record_date', models.DateTimeField()),
                ('record_broken_date', models.DateTimeField()),
            ],
        ),
    ]
