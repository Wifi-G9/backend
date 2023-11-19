from main_page.views.word_search_view import WordSearch
from main_page.views.instagram_search_view import InstagramSearch
from main_page.views.chatgpt_description_view import ChatGPTDescription
from main_page.views.similar_trends import SimilarTrends
from main_page.views.popular_trends import PopularTrends
from main_page.views.interest_over_time import InterestOverTime
from main_page.views.sentiment_analysis import SentimentAnalysis
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', WordSearch.as_view()),
    path('search-instagram', InstagramSearch.as_view()),
    path('describe', ChatGPTDescription.as_view()),
    path('similar-trends', SimilarTrends.as_view()),
    path('popular-trends', PopularTrends.as_view()),
    path('interest-over-time', InterestOverTime.as_view()),
    path('sentiment-analysis', SentimentAnalysis.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
