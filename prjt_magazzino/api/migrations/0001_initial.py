# Generated by Django 3.2.19 on 2023-05-05 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizzazione',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Utenti',
            },
        ),
        migrations.CreateModel(
            name='Utente_Organizzazione',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organizzazione', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='utenti', to='api.organizzazione')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Utenti_Organizzazioni',
            },
        ),
        migrations.CreateModel(
            name='Unita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_boxes', models.PositiveIntegerField()),
                ('organizzazione', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutte_unita', to='api.organizzazione')),
            ],
            options={
                'verbose_name_plural': 'Unita',
            },
        ),
        migrations.CreateModel(
            name='Scatola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descrizione', models.TextField(blank=True, default='')),
                ('quantita', models.PositiveIntegerField(default=0)),
                ('unita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scatole', to='api.unita')),
            ],
            options={
                'verbose_name_plural': 'Scatole',
            },
        ),
    ]
