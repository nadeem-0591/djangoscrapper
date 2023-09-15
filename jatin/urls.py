
from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('scrape_properties/', views.scrape_properties_view, name='scrape_properties'),
]