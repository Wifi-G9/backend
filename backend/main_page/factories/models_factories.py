import factory
from django.contrib.auth.hashers import make_password
from factory.django import DjangoModelFactory

from main_page.models.user import User
from main_page.models.accounts import Accounts
from main_page.models.developer_message import DeveloperMessage
from main_page.models.search_history import SearchHistory
from main_page.models.word_history import WordHistory
from main_page.models.word_of_the_day import WordOfTheDay


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    name = factory.Faker('name')
    age = factory.Faker('random_int', min=18, max=99)
    email = factory.Faker('email')
    password = factory.Faker('password')


class AccountsFactory(DjangoModelFactory):
    class Meta:
        model = Accounts

    user = factory.SubFactory(UserFactory)
    instagram_access_token = factory.Faker('uuid4')
    twitter_access_token = factory.Faker('uuid4')
    facebook_access_token = factory.Faker('uuid4')


class DeveloperMessageFactory(DjangoModelFactory):
    class Meta:
        model = DeveloperMessage

    user = factory.SubFactory(UserFactory)
    message = factory.Faker('text')
    timestamp = factory.Faker('date_time_this_year')


class SearchHistoryFactory(DjangoModelFactory):
    class Meta:
        model = SearchHistory

    user = factory.SubFactory(UserFactory)
    timestamp = factory.Faker('date_time_this_year')
    search_query = factory.Faker('word')


class WordHistoryFactory(DjangoModelFactory):
    class Meta:
        model = WordHistory

    word = factory.Faker('word')
    timestamp = factory.Faker('date_time_this_year')


class WordOfTheDayFactory(DjangoModelFactory):
    class Meta:
        model = WordOfTheDay

    word = factory.Faker('word')
    timestamp = factory.Faker('date_time_this_year')
