from django.urls import path
from .views import ArtisteList, ArtisteDetail, SongList, SongDetail

urlpatterns = [
    path('artiste/<int:pk>/', ArtisteDetail.as_view()),
    path('artiste', ArtisteList.as_view()),
    path('song/<int:pk>/', SongDetail.as_view()),
    path('song/', SongList.as_view()),
]
