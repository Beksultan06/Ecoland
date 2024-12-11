from django.urls import path
from app.tour.views import TourView

urlpatterns = [
    path("tour", TourView.as_view(), name='tour')
]
