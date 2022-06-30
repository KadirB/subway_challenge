from django.urls import include, path

from mainapp import views

urlpatterns = [
    path('index/', views.index, name='home-page'),
    path('profile/<str:username>/', views.profile, name='profile-page'),
    path('meal/<str:name>/', views.meal, name='meal-page'),
    # path('meal/<str:name>/<str:username>/<int:token>/', views.section, name='article-section'),
]