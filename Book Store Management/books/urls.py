from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import add_book

urlpatterns = [
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('login/',views.user_login,name='login'),
    path('Signup/',views.signup,name='Signup'),
    path('Home/',views.home,name='Home'),
    path('add/', views.add_book, name='add'),
    path('delete/',views.delete_book,name='delete'),
    path('logout/',views.logout, name='logout'),
    path('show/',views.book_list,name='show'),

]