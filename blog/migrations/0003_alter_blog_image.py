# Generated by Django 4.1.5 on 2023-01-22 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_blog_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="image",
            field=models.ImageField(upload_to="img/"),
        ),
    ]
