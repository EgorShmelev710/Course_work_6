# Generated by Django 4.2 on 2024-06-07 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_token'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('deactivate_user', 'Can deactivate user'), ('view_all_users', 'Can view all users')], 'verbose_name': 'рассылка', 'verbose_name_plural': 'рассылки'},
        ),
    ]
