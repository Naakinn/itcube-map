# pages/urls.py
from django.urls import path
from .views import homePageView, searchView, resultsView
 
urlpatterns = [
    path('', homePageView, name='home'),
    path('search/', searchView, name='search-view'),
    path('results/', resultsView, name='results-view')
]
