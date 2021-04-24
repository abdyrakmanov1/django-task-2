from django.urls import path
from .views import main_page, novelty, CreateBook

urlpatterns = [
    path('', main_page, name='main_page'),
    path('novelty', novelty, name='novelty'),
    path('add/', CreateBook.as_view(), name='upload_book'),
]