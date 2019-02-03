# Generated by Django 2.1.5 on 2019-02-03 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleryweb', '0004_multimedia_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multimedia',
            name='archivoImagen',
        ),
        migrations.AddField(
            model_name='multimedia',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='files'),
        ),
    ]
