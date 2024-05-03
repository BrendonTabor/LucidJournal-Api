# Generated by Django 4.2.11 on 2024-05-02 16:14

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
            name='DreamFactor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='RemCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cycles_completed', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SleepFactor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WakeMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('date_recorded', models.DateField(default='0000-00-00')),
                ('dreamfactors', models.ManyToManyField(related_name='entries', through='LucidJournalapi.DreamFactor', to='LucidJournalapi.sleepfactor')),
                ('rem_count', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LucidJournalapi.remcount')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to=settings.AUTH_USER_MODEL)),
                ('wake_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LucidJournalapi.wakemethod')),
            ],
        ),
        migrations.AddField(
            model_name='dreamfactor',
            name='entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LucidJournalapi.entry'),
        ),
        migrations.AddField(
            model_name='dreamfactor',
            name='sleepfactor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LucidJournalapi.sleepfactor'),
        ),
    ]
