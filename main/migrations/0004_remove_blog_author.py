# Generated by Django 3.1.4 on 2020-12-23 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_blog_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
    ]
