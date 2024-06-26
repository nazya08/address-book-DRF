# Generated by Django 5.0.1 on 2024-01-16 19:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_alter_events_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='url',
            field=models.URLField(),
        ),
        migrations.CreateModel(
            name='ContactActivityLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(choices=[('CREATED', 'Created'), ('EDITED', 'Edited')], max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('details', models.TextField()),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.contact')),
            ],
        ),
    ]
