from django.urls import path, include
from . import views

app_name = 'HomeApp'


urlpatterns = [

    path('', views.index_view, name='home'),

    path('events/', views.events, name='events'),
    path('events/<int:pk>/', views.upcoming_events, name='upcoming-event'),
    path('gallery/', views.gallery_view, name='gallery-view'),
    path('aboutus/', views.about_us_view, name='aboutus-view'),
    path('contact/', views.contact_view, name='contact-view'),
]