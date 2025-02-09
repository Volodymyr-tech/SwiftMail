# Generated by Django 5.1.6 on 2025-02-09 18:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailingAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_attempt', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Success', 'Success'), ('Error', 'Error')], max_length=10)),
                ('server_response', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Mailing Attempt',
                'verbose_name_plural': 'Mailing Attempts',
                'ordering': ['-date_attempt'],
            },
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_sending', models.DateTimeField(null=True)),
                ('end_sending', models.DateTimeField(null=True)),
                ('status', models.CharField(choices=[('Sent', 'Sent'), ('Sending', 'Sending'), ('Created', 'Created')], default='Created', max_length=10)),
                ('client', models.ManyToManyField(to='clients.client')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mails', to='message.message')),
            ],
            options={
                'verbose_name': 'Mail',
                'verbose_name_plural': 'Mails',
                'ordering': ['-first_sending'],
            },
        ),
    ]
