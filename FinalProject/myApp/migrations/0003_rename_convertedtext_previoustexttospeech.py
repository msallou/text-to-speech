# Generated by Django 4.2.9 on 2024-06-03 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_rename_convertedtexts_convertedtext'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ConvertedText',
            new_name='PreviousTextToSpeech',
        ),
    ]
