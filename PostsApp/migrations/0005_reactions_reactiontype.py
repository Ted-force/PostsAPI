# Generated by Django 4.0.2 on 2022-03-15 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostsApp', '0004_reactions_rename_likescount_post_reactionscount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reactions',
            name='reactionType',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
