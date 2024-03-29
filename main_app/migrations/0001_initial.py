# Generated by Django 5.0.2 on 2024-02-16 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_species', models.CharField(max_length=100)),
                ('scientific_name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('habitat', models.CharField(max_length=250)),
                ('diet', models.CharField(max_length=250)),
                ('average_lifespan', models.CharField(max_length=50)),
                ('image_url', models.URLField()),
            ],
        ),
    ]
