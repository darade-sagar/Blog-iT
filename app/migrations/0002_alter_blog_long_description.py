# Generated by Django 4.1.6 on 2023-02-12 05:32

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='long_description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]