from django.views.generic import TemplateView
from app.destinations.services import DestinationsService

class DestinationsView(TemplateView):
    template_name = 'destinations/destinations.html'

    def get_context_data(self, **kwargs):
        """Передаем все направления в контекст."""
        context = super().get_context_data(**kwargs)
        context['destinations_all'] = DestinationsService.get_all_destinations()
        return context


class DestinationsDetailsView(TemplateView):
    template_name = 'destinations/destinations-details.html'

    def get_context_data(self, **kwargs):
        """Передаем детали направления в контекст."""
        context = super().get_context_data(**kwargs)
        destination = DestinationsService.get_destination_by_id(kwargs['pk'])
        if destination is None:
            context['error'] = "Направление не найдено"
            return context
        destination_details = DestinationsService.get_destination_details_by_destination(destination)
        destination_details_pynkt = DestinationsService.get_all_destinationspynkt()

        context['destination_id'] = destination
        context['destination_details'] = destination_details
        context['destination_details_pynkt'] = destination_details_pynkt
        return context