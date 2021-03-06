# Generated by Django 3.2.11 on 2022-05-12 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('year', models.CharField(blank=True, max_length=4, null=True)),
                ('rated', models.CharField(default='N/A', max_length=255)),
                ('released', models.CharField(blank=True, max_length=50, null=True)),
                ('runtime', models.CharField(blank=True, max_length=20, null=True)),
                ('genre', models.CharField(blank=True, max_length=50, null=True)),
                ('director', models.CharField(blank=True, max_length=100, null=True)),
                ('writer', models.CharField(blank=True, max_length=100, null=True)),
                ('actors', models.CharField(blank=True, max_length=255, null=True)),
                ('plot', models.TextField(blank=True, max_length=1000, null=True)),
                ('language', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('awards', models.CharField(default='N/A', max_length=255)),
                ('poster', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
                'ordering': ['-year'],
            },
        ),
    ]
