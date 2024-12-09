from django.urls import path
from app.news.views import NewsView, NewsDetailsView

urlpatterns = [
    path('news', NewsView.as_view(), name='news'),
    path("news-detail/<int:id>/", NewsDetailsView.as_view(), name='news-detail')
]
