from django.contrib import admin
from django.urls import path
from movies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.test),
    path('movies/', views.movie_list_view),
    path('movies/<int:id>/', views.movie_detail_view),
]