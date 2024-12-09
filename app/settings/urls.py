from django.urls import path
from app.settings.views import index, AboutPageView, contact

urlpatterns = [
    path("", index, name='index'),
    path('about/', AboutPageView.as_view(), name='about'),
    path("contact", contact, name='contact'),
]
