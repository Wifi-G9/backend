from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from user_page.views.music_suggestion_view import MusicSuggestion

urlpatterns = [
    path('description-deezer', MusicSuggestion.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
