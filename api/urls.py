from .views import main, authors, get_author, create_author, delete_author
from django.urls import path


urlpatterns = [
    path(' ',  main,  name="home-view"),
    path('authors/', authors, name='all-authors'),
    path('authors/<int:id>', get_author, name='author'),
    path('authors/create/', create_author, name='create-author'),
    path('authors/delete/<int:id>', delete_author, name='delete-author')

]
