# Generated by Django 5.1.4 on 2024-12-25 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0002_remove_game_buyer_game_buyer'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]