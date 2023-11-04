from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from main_page.views.main_page_view import MainPageView

urlpatterns = [
    path('', MainPageView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)