# Generated by Django 4.2.5 on 2023-09-11 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy_blog', '0003_alter_article_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
