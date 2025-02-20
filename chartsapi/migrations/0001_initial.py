# Generated by Django 5.1.1 on 2024-09-23 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MonthData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=2)),
                ('time_data', models.ManyToManyField(to='chartsapi.timedata')),
            ],
        ),
        migrations.CreateModel(
            name='YearData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4)),
                ('month_data', models.ManyToManyField(to='chartsapi.monthdata')),
            ],
        ),
    ]
