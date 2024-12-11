from django.shortcuts import render, redirect
from app.news.models import NewsPage, NewsListDetails, NewsComment
from django.views.generic import TemplateView
from django.core.paginator import Paginator

class NewsView(TemplateView):
    template_name = 'news/news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_id'] = NewsPage.objects.latest("id")  # Берем последнюю новость
        context['news_list_all'] = NewsListDetails.objects.all()  # Все новости
        return context

class NewsDetailsView(TemplateView):
    template_name = 'news/news-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news = NewsListDetails.objects.get(id=kwargs['id'])
        context['news'] = news
        comments = NewsComment.objects.filter(news=news)
        paginator = Paginator(comments, 5)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['news_comment'] = page_obj
        context['page_obj'] = page_obj
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('message')

        if name and email and comment:
            NewsComment.objects.create(name=name, email=email, comment=comment, news_id=kwargs['id'])

        return redirect('news:news-detail', id=kwargs['id'])
