from django.shortcuts import render
from django.views.generic import TemplateView
from app.destinations.models import DestinationsModels, DestinationsDetailModels
from django.shortcuts import get_object_or_404

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
        destination_id = get_object_or_404(DestinationsModels, pk=kwargs['pk'])
        destination_details = DestinationsDetailModels.objects.filter(destination=destination_id)
        context['destination_id'] = destination_id
        context['destination_details'] = destination_details

        return context