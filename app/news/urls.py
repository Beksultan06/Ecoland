from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from app.news.views import NewsView, NewsDetailsView

app_name = 'news'

urlpatterns = (
    path('news/', NewsView.as_view(), name='news'),
    path('news-detail/<int:id>/', NewsDetailsView.as_view(), name='news-detail'),
)
