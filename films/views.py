from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import AddReviewForm
from .models import Film, Genre, Reviews

menu = [
        {'title': 'Каталог фильмов', 'url_name': 'home'},
        ]


# class NatureHome(ListView):
#     model = Nature
#     template_name = 'nature/index.html'
#     context_object_name = 'posts'
#     # extra_context = {'title': 'Главная страница'}

# def get_context_data(self, *, object_list=None, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context['menu'] = menu
#     context['title'] = 'Главная страница!'
#     context['cat_selected'] = 0
#     return context
#
# def get_queryset(self):
#     return Nature.objects.filter(is_published=True)


# class FilmsIndex(ListView):
#     paginate_by = 25
#     model = Film
#     template_name = 'films/index.html'
#     context_object_name = 'films'
#     # extra_context = {'title': 'Главная страница'}
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         print(context)
#         print('reqiestt!')
#         print(self.request)
#         # context['films'] = films
#         context['menu'] = menu
#         # context['title'] = 'Каталог фильмов'
#         context['genre_selected'] = 0
#         return context
#
#     def get_queryset(self):
#         return Film.objects.all()

def index(request):
    films = Film.objects.all()
    # for film in films:
    #     marks = list(map(lambda x: x.rating, Reviews.objects.filter(film_id=film.id)))
    #     if marks:
    #         film.rating = sum(marks)//len(marks)
    #     else:
    #         film.rating = 0

    if request.method == 'POST':
        if request.POST.get('sort_by'):
            sorting = request.POST['sort_by']
            films = films.order_by(sorting)

    paginator = Paginator(films, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'films': films,
        'menu': menu,
        'title': 'Каталог фильмов',
        'genre_selected': 0,
        'page_obj': page_obj,
        'genre_slug': ''}

    return render(request, 'films/index.html', context=context)

def profile(request):
    reviews = Reviews.objects.filter(user_id=request.user.id)

    context = {
        'menu': menu,
        'reviews': reviews
    }
    return render(request, 'films/profile.html', context=context)


# def show_genre(request, genre_slug):
#     return HttpResponse(f'<h1>Жанры фильмов</h1><p>{genre_slug}</p>')

def show_genre(request, genre_slug):
    genre = Genre.objects.filter(slug=genre_slug)


    if len(genre) == 0:
        raise Http404

    id = genre[0].id
    films = Film.objects.filter(genre_id=id)
    if request.method == 'POST':
        if request.POST.get('sort_by'):
            sorting = request.POST['sort_by']
            films = films.order_by(sorting)
    paginator = Paginator(films, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'films': films,
        'menu': menu,
        'page_obj': page_obj,
        'genre_slug': genre_slug
    }

    return render(request, 'films/index.html', context=context)


def show_film(request, genre_slug, film_slug):
    film = Film.objects.filter(slug=film_slug)[0]
    reviews = Reviews.objects.filter(film_id=film.id)
    print(film.rating)
    context = {
        'menu': menu,
        'film': film,
        'genre_slug': genre_slug,
        'reviews': reviews
    }
    return render(request, 'films/film.html', context=context)


def leave_review(request, film_slug):
    if request.method == 'POST':
        form = AddReviewForm(request.POST, request.FILES)
        text = request.POST['review_text']
        rating = request.POST['rating']
        film = Film.objects.filter(slug=film_slug)[0]
        film_id = film.id
        film_title = film.title
        review = Reviews(review_text=text, user_id=request.user.id, film_title=film_title, rating=rating, film_id=film_id)
        try:
            review.save()
        except Exception:
            print('ошибка')
        all_film_marks = list(map(lambda x: x.rating, Reviews.objects.filter(film_id=film.id)))
        total_film_rating = sum(all_film_marks) // len(all_film_marks) if all_film_marks else 0
        Film.objects.filter(id=film_id).update(rating=total_film_rating)
        return redirect('profile')
    else:
        form = AddReviewForm()
        print(form)


    context = {
        'form': form,
        'film_slug': film_slug
    }
    return render(request, 'films/leave_review.html', context=context)


# def login(request):
#     pass


# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST, request.FILES)
#         username = request.POST['username']
#         password = request.POST['password']
#         try:
#             user = User(username=username, password=password)
#             user.save()
#             return redirect('profile')
#         except:
#             print('ошибка')
#     else:
#         form = RegisterForm()
#         print(form)

    # context = {
    #     'form': form
    # }
    # return render(request, 'films/register.html', context=context)

class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'films/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'films/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('profile')

def logout_user(request):
    logout(request)
    return redirect('login')
