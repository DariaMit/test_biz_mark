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
# urlpatterns = [
#     path('', NatureHome.as_view(), name='home'),
#     path('about/', about, name='about'),
#     path('add_page/', AddPage.as_view(), name='add_page'),
#     path('contact/', contact, name='contact'),
#     path('login/', login, name='login'),
#     path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
#     path('category/<slug:cat_slug>/', ShowCategory.as_view(), name='category'),
# ]