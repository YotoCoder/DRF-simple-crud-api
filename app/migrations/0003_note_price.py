# Generated by Django 4.1.1 on 2022-09-17 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_note_delete_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='price',
            field=models.FloatField(default=100),
            preserve_default=False,
        ),
    ]