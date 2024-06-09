# Generated by Django 4.2 on 2024-06-08 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='заголовок')),
                ('content', models.TextField(verbose_name='содержимое статьи')),
                ('image', models.ImageField(upload_to='mailing_images/', verbose_name='изображение')),
                ('views_count', models.IntegerField(default=0, verbose_name='просмотры')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'блог',
                'verbose_name_plural': 'блоги',
            },
        ),
    ]
