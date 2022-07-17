from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=226)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def get_absolute_url(self):
        return reverse('genre', kwargs={'genre_slug': self.slug})

    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.CharField(max_length=226)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    actors = models.TextField(blank=True)
    director = models.TextField(blank=True)
    preview_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    # gallery_photos = models.ImageField(upload_to='photos/%Y/%m/%d/')
    production_date = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)

    # film1 = Film(title='Reservoir Dogs', production_date='1991-10-8', slug='reservoir-dogs', actors='Tim Roth, Stive Bushemi', director='Quentin Tarantino', genre_id=1)
    # film2 = Film(title='The Big Lebowski', production_date='2013-3-28', slug='the-big-lebowski', actors='Jeff Bridges, Stive Bushemi', director='Joel Coen, Ethan Coen', genre_id=2)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('film', kwargs={'film_slug': self.slug, 'genre_slug': self.genre.slug})

    def get_leave_review_url(self):
        print(reverse('leave_review', kwargs={'film_slug': self.slug}))
        return reverse('leave_review', kwargs={'film_slug': self.slug})

    # class Meta:
    #     verbose_name = 'Природа моя природа'
    #     verbose_name_plural = 'Природа моя природа'
    #     ordering = ['time_create', 'title']

class Review(models.Model):
    pass
    # review_text = models.TextField()
    # film_title = models.TextField()
    # user = models.ForeignKey(User, on_delete=models.PROTECT)
    # film = models.ForeignKey(Film, on_delete=models.PROTECT)
    # rating = models.IntegerField()


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='gallery_images')

class Reviews(models.Model):
    review_text = models.TextField()
    film_title = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    film = models.ForeignKey(Film, on_delete=models.PROTECT)
    rating = models.IntegerField()