from django.urls import include, path

from mainapp import views

urlpatterns = [
    path('logout', views.logout_view, name='logout'),
    path('', views.home, name='home-page'),
    path('profile/<str:username>/<str:token>/', views.profile, name='profile-page'),
    path('profile/order/<int:id>/<str:username>/<str:token>/', views.order, name='order'),
    path('meal/<str:name>/<str:username>/<str:token>/', views.meal, name='meal-page'),
]