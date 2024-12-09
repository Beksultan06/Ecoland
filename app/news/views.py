from django.shortcuts import render
from app.news.models import NewsPage, NewsList
from django.views.generic import TemplateView

class NewsView(TemplateView):
    template_name = 'news/news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_id'] = NewsPage.objects.latest("id")
        context['news_list_all'] = NewsList.objects.all()
        return context

class NewsDetailsView(TemplateView):
    template_name = 'news/news-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = NewsList.objects.latest("id")
        return context
