# Generated by Django 3.1.5 on 2021-03-02 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispositions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='disposition',
            name='clave',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
