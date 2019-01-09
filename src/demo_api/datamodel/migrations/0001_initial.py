# Generated by Django 2.1.4 on 2019-01-08 12:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, help_text='Unieke resource identifier (UUID4)', unique=True)),
                ('tekst', models.CharField(help_text='De tekst van de quote.', max_length=200, verbose_name='quote')),
                ('aangemaakt', models.DateTimeField(auto_now_add=True, help_text='Datum en tijd van wanneer het object is aangemaakt.', verbose_name='aangemaakt')),
            ],
            options={
                'verbose_name': 'quote',
                'verbose_name_plural': 'quotes',
                'ordering': ('tekst',),
            },
        ),
    ]
