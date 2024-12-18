from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# class TourView(TemplateView):
#     template_name = 'tour/tour.html'

#     def get_context_data(self, **kwargs):
#         pass


def tour(request):
    return render(request, "tour/tours.html", locals())

def tour_details(request):
    return render(request, 'tour/tour-details.html', locals())