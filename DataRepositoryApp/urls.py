from django.conf.urls import url
from django.urls import path, include
from . import views

app_name = 'DataRepositoryApp'


urlpatterns = [

    path('alumni/', views.get_all_alumni, name='get-alumni'),
    path('session/<session>/', views.get_by_session, name='get-session'),
    path('profile/<int:pk>/', views.get_profile_by_id, name='get-profile'),
    path('search/', views.search_result, name='search-result')
]
