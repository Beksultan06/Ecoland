from django.shortcuts import render
from django.views.generic import TemplateView
from app.destinations.models import DestinationsModels

class DestinationsView(TemplateView):
    template_name = 'destinations/destinations.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['destinations_all'] = DestinationsModels.objects.all()
        return context

class DestinationsDetailsView(TemplateView):
    template_name = 'destinations/destinations-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context