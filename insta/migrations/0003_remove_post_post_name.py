# Generated by Django 4.0.5 on 2022-06-05 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_post_comments_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_name',
        ),
    ]