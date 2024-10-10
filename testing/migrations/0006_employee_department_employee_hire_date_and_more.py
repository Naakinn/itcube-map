# Generated by Django 5.1.1 on 2024-10-10 15:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0005_department_profile_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='testing.department'),
        ),
        migrations.AddField(
            model_name='employee',
            name='hire_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='projects',
            field=models.ManyToManyField(to='testing.project'),
        ),
        migrations.AddField(
            model_name='profile',
            name='employee',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='testing.employee'),
        ),
    ]
