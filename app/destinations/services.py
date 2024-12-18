from django.core.exceptions import ObjectDoesNotExist
from app.destinations.models import DestinationsModels, DestinationsDetailModels, DestinationsPynkt

class DestinationsService:
    @staticmethod
    def get_all_destinations():
        return DestinationsModels.objects.all()

    @staticmethod
    def get_all_destinationspynkt():
        return DestinationsPynkt.objects.all()

    @staticmethod
    def get_destination_by_id(id):
        try:
            return DestinationsModels.objects.get(id=id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def get_destination_details_by_destination(destination):
        return DestinationsDetailModels.objects.filter(destination=destination)
