# Generated by Django 4.2.6 on 2023-10-23 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_events_contacts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='events',
            options={'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
    ]
