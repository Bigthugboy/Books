from django.urls import path
from . import views


app_name = 'first_app'

urlpatterns = [
    path('<str:name>/<int:num>', views.hello),
    path('', views.index),

    path('book-list/', views.book_list, name='book-list'),
    path('book-list-fiction/', views.book_list_for_fiction, name='book-list-fiction'),
    path('book-list-price/', views.book_list_for_price, name='book-list-price'),
    path('book-detail/<int:pk>/', views.book_detail, name='book-detail'),
    path('redirect/', views.redirect),


]