from django import template
from films.models import Genre, Film

register = template.Library()


@register.simple_tag(name='getgenres')
def get_genres(filter=None):
    if not filter:
        return Genre.objects.all()
    else:
        return Genre.objects.filter(pk=filter)

@register.inclusion_tag('films/list_genres.html')
def show_genres(sort=None, genre_selected=0):
    if not sort:
        genres = Genre.objects.all()
    else:
        genres = Genre.objects.order_by(sort)

    return {"genres": genres, "genre_selected": genre_selected}