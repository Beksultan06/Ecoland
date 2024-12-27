from app.tour.models import Tour, Settings

class TourServices:
    def tour_all_services():
        return Tour.objects.all()

    def settings_tour_id_services():
        return Settings.objects.latest("id")