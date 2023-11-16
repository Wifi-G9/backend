from main_page.views.main_page_view import MainPageView
from main_page.views.sentiment_analysis import SentimentAnalysis
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from main_page.views.word_search_view import WordSearch

urlpatterns = [
    path('', MainPageView.as_view()),
    path('sentiment-analysis/', SentimentAnalysis.as_view(), name='sentiment_analysis'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
