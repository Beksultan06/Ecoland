from django.shortcuts import redirect
from django.views.generic import TemplateView
from app.news.services import NewsService

class NewsView(TemplateView):
    template_name = 'news/news.html'

    def get_context_data(self, **kwargs):
        """Передача данных для отображения списка новостей."""
        context = super().get_context_data(**kwargs)
        context['news_id'] = NewsService.get_latest_news()
        context['news_list_all'] = NewsService.get_all_news()
        return context

class NewsDetailsView(TemplateView):
    template_name = 'news/news-details.html'

    def get_context_data(self, **kwargs):
        """Передача данных для отображения деталей новости и комментариев."""
        context = super().get_context_data(**kwargs)
        news = NewsService.get_news_details(kwargs['id'])
        page_number = self.request.GET.get('page')
        page_obj = NewsService.get_paginated_comments(news, page_number)

        context['news'] = news
        context['news_comment'] = page_obj
        context['page_obj'] = page_obj
        return context

    def post(self, request, *args, **kwargs):
        """Обработка формы комментариев."""
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('message')

        if name and email and comment:
            NewsService.create_comment(name, email, comment, kwargs['id'])

        return redirect('news:news-detail', id=kwargs['id'])
