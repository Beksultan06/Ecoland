from django.http import Http404
from django.views.generic import TemplateView
from app.destinations.services import DestinationsService


class DestinationsView(TemplateView):
    template_name = 'destinations/destinations.html'

    def get_context_data(self, **kwargs):
        """Передаем все направления в контекст."""
        context = super().get_context_data(**kwargs)
        destinations = DestinationsService.get_all_destinations()
        context['destinations_all'] = destinations
        return context

class DestinationsDetailsView(TemplateView):
    template_name = 'destinations/destinations-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            destination = DestinationsService.get_destination_by_id(kwargs['id'])
            if not destination:
                raise Http404("Направление не найдено")

            destination_details = DestinationsService.get_destination_details_by_destination(destination)
            destination_details_pynkt = DestinationsService.get_all_destinationspynkt()

            context.update({
                'destination_id': destination,
                'destination_details': destination_details,
                'destination_details_pynkt': destination_details_pynkt,
            })

        except Exception as e:
            context['error'] = str(e)

        return context