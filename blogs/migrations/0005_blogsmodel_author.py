# Generated by Django 5.1.4 on 2024-12-24 09:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_alter_authorsmodel_options_alter_blogsmodel_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogsmodel',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blogs.authorsmodel'),
            preserve_default=False,
        ),
    ]
