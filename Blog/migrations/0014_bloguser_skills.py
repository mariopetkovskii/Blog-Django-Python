# Generated by Django 4.0.5 on 2022-06-02 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0013_rename_comment_by_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloguser',
            name='skills',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
