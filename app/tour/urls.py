from django.urls import path
from app.tour.views import tour, tour_details

urlpatterns = [
    path("tour", tour, name='tour'),
    path("tour_details", tour_details, name='tour_details'),

]
