# Generated by Django 5.0.1 on 2024-01-15 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_typ'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='Images/None/default.jpg', upload_to='Images/'),
        ),
    ]