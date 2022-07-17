from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('profile/', profile, name='profile'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('leave_review/<slug:film_slug>', leave_review, name='leave_review'),
    path('<slug:genre_slug>/', show_genre, name='genre'),
    path('<slug:genre_slug>/<slug:film_slug>', show_film, name='film'),
]
