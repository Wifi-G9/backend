# Django User Management System

This is a Django application for managing user accounts, developer messages, and search history.

## Models

### Accounts

- `id` (Primary Key)
- `instagram_access_token`
- `twitter_access_token`
- `facebook_access_token`

### DeveloperMessage

- `id` (Primary Key)
- `message`
- `timestamp`
- `user` (Foreign Key to User)

### SearchHistory

- `id` (Primary Key)
- `user` (Foreign Key to User)
- `timestamp`
- `search_query`

### User

- `id` (Primary Key)
- `name`
- `age`
- `email`
- `password`
- `accounts` (One-to-One relationship with Accounts)

## Serializers

### AccountsSerializer

Serializes the `Accounts` model.

### SearchHistorySerializer

Serializes the `SearchHistory` model.

### UserSerializer

Serializes the `User` model.

## Usage

You can use the provided serializers in your Django REST Framework views to interact with the models. For example, you can use the `UserSerializer` to create, retrieve, update, and delete user records.

```python
# Example view using UserSerializer
from rest_framework import generics

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
