# Generated by Django 4.0.5 on 2022-06-03 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0014_bloguser_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
    ]