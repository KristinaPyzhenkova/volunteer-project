# Generated by Django 2.2.16 on 2022-06-06 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20220530_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='marker',
            field=models.TextField(null=True, verbose_name='Маркер'),
        ),
    ]
