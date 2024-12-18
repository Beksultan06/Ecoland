from django.urls import path
from app.destinations.views import DestinationsView, DestinationsDetailsView

urlpatterns = [
    path("destinations", DestinationsView.as_view(), name='destinations'),
    path('destinations/<int:id>/', DestinationsDetailsView.as_view(), name='destinations-details'),
]