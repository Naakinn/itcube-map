from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    path('', homePageView, name="home"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name="login_view"),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout_view"),
    path("search/", searchView, name="search_view"),
    path("results/", resultsView, name="results_view"),
    path("books/", BookListView.as_view(), name="book_list_view"),
    path("books/create/", BookCreateView.as_view(), name="book_create_view"),
    path("books/<int:pk>/edit/", BookUpdateView.as_view(), name="book_update_view"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book_detail_view"),
    path("books/<int:pk>/delete/", book_delete_view, name="book_delete_view"),
]
