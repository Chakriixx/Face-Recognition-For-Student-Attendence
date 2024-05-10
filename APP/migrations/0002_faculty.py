# Generated by Django 5.0.4 on 2024-05-04 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_id', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=30)),
                ('DOB', models.DateField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('qualification', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=400)),
            ],
            options={
                'db_table': 'faculty',
            },
        ),
    ]