# Generated by Django 4.0.5 on 2022-06-02 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_alter_bloguser_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Blog.bloguser'),
        ),
    ]
