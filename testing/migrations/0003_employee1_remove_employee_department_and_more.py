# Generated by Django 5.1.1 on 2024-10-10 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0002_test_employee_department_employee_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='department',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='projects',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
