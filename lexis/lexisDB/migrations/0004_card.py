# Generated by Django 3.2.3 on 2021-06-05 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lexisDB', '0003_word_theme'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=100)),
                ('created', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lexisDB.profile')),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lexisDB.word')),
            ],
        ),
    ]
