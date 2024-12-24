# Generated by Django 5.1.4 on 2024-12-24 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='buyer',
        ),
        migrations.AddField(
            model_name='game',
            name='buyer',
            field=models.ManyToManyField(related_name='games', to='task1.buyer'),
        ),
    ]
