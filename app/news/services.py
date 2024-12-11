from django.core.paginator import Paginator
from app.news.models import NewsListDetails, NewsComment

class NewsService:
    @staticmethod
    def get_latest_news():
        """Получить последнюю новость."""
        return NewsListDetails.objects.latest("id")

    @staticmethod
    def get_all_news():
        """Получить все новости."""
        return NewsListDetails.objects.all()

    @staticmethod
    def get_news_details(news_id):
        """Получить детали конкретной новости."""
        return NewsListDetails.objects.get(id=news_id)

    @staticmethod
    def get_paginated_comments(news, page_number, per_page=5):
        """Получить комментарии с пагинацией."""
        comments = NewsComment.objects.filter(news=news)
        paginator = Paginator(comments, per_page)
        return paginator.get_page(page_number)

    @staticmethod
    def create_comment(name, email, comment, news_id):
        """Создать новый комментарий."""
        return NewsComment.objects.create(
            name=name,
            email=email,
            comment=comment,
            news_id=news_id
        )
