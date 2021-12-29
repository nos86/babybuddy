# Generated by Django 3.2.10 on 2021-12-29 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_sleep_napping'),
    ]

    operations = [
        migrations.CreateModel(
            name='Height',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.FloatField(verbose_name='Height')),
                ('date', models.DateField(verbose_name='Date')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='height', to='core.child', verbose_name='Child')),
            ],
            options={
                'verbose_name': 'Height',
                'verbose_name_plural': 'Height',
                'ordering': ['-date'],
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='HeadCircumference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head_circumference', models.FloatField(verbose_name='Head Circumference')),
                ('date', models.DateField(verbose_name='Date')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='head_circumference', to='core.child', verbose_name='Child')),
            ],
            options={
                'verbose_name': 'Head Circumference',
                'verbose_name_plural': 'Head Circumference',
                'ordering': ['-date'],
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
        migrations.CreateModel(
            name='BMI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bmi', models.FloatField(verbose_name='BMI')),
                ('date', models.DateField(verbose_name='Date')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bmi', to='core.child', verbose_name='Child')),
            ],
            options={
                'verbose_name': 'BMI',
                'verbose_name_plural': 'BMI',
                'ordering': ['-date'],
                'default_permissions': ('view', 'add', 'change', 'delete'),
            },
        ),
    ]