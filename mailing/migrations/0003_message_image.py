# Generated by Django 5.0.6 on 2024-05-30 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0002_alter_mailing_regularity'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='mailing_images/', verbose_name='картинка'),
        ),
    ]
