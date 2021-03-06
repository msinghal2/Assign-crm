# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 21:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.CharField(max_length=10)),
                ('floor', models.CharField(max_length=20)),
                ('room', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeName', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=25)),
                ('photo', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='EmpName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assign.EmployeeInfo'),
        ),
    ]
