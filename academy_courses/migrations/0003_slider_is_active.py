# Generated by Django 4.2.5 on 2023-09-08 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy_courses', '0002_remove_course_category_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='is_active',
            field=models.CharField(choices=[('', 'Select status'), ('active', 'Active'), (' ', 'Inactive')], default='Select status', max_length=50),
        ),
    ]
