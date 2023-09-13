# Generated by Django 4.2.5 on 2023-09-12 19:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academy_courses', '0014_remove_course_video_delete_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=1000)),
                ('video', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mov', 'avi', 'mp4', 'webm', 'mkv', 'wmv', 'ogg'])])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy_courses.course')),
            ],
        ),
    ]