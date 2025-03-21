# Generated by Django 5.1.6 on 2025-02-09 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(help_text='Enter the mailing list topic', max_length=255, verbose_name='Mailing list topic')),
                ('body', models.TextField(help_text='Enter the mailing text', verbose_name='Mailing text')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
    ]
