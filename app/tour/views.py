from django.shortcuts import render
from django.views.generic import TemplateView
from app.tour.service import TourServices

def tour(request):
    tour_all = TourServices.tour_all_services()
    tour_id = TourServices.settings_tour_id_services()
    return render(request, "tour/tours.html", locals())

def tour_details(request):
    return render(request, 'tour/tour-details.html', locals())