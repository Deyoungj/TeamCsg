# Generated by Django 4.1.1 on 2022-09-22 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('price', models.FloatField()),
                ('months', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=7)),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('student_id', models.CharField(default='8oCsG7lctYJ7Uxc', max_length=20, unique=True)),
                ('image', models.FileField(upload_to='images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PackageEnroled',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_enrolled', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField(null=True)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='packages', to='students.package')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='students.student')),
            ],
        ),
    ]
