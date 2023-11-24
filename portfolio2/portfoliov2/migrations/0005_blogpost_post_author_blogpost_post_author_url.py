# Generated by Django 4.2.7 on 2023-11-07 13:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfoliov2", "0004_personalinfo_linkedin_link"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="post_author",
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="blogpost",
            name="post_author_url",
            field=models.URLField(default="https://twitter.com/Sdecipher"),
        ),
    ]