# Generated by Django 5.0.2 on 2024-02-27 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detectionresult',
            old_name='gender',
            new_name='maladie',
        ),
        migrations.RemoveField(
            model_name='detectionresult',
            name='age',
        ),
        migrations.RemoveField(
            model_name='detectionresult',
            name='hair_color',
        ),
        migrations.RemoveField(
            model_name='detectionresult',
            name='skin_color',
        ),
        migrations.AlterField(
            model_name='detectionresult',
            name='image',
            field=models.ImageField(upload_to='lung_image/'),
        ),
    ]