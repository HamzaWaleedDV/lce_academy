# Generated by Django 4.2.5 on 2023-09-12 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy_courses', '0015_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(default='test test', max_length=5000),
            preserve_default=False,
        ),
    ]