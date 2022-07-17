# Generated by Django 4.0.6 on 2022-07-16 19:30

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
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=226)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('actors', models.TextField(blank=True)),
                ('director', models.TextField(blank=True)),
                ('preview_photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('production_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=226)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField()),
                ('film_title', models.TextField()),
                ('rating', models.IntegerField()),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='films.film')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='films.film')),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='films.genre'),
        ),
    ]
