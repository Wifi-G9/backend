# Django User Management System

This is a Django application for managing user accounts, developer messages, and search history.

## Models

### Accounts

- `instagram_access_token`
- `twitter_access_token`
- `facebook_access_token`

### DeveloperMessage

- `message`
- `timestamp`
- `user` (Foreign Key to User)

### SearchHistory

- `user` (Foreign Key to User)
- `timestamp`
- `search_query`

### User

- `name`
- `age`
- `email`
- `password`
- `accounts` (One-to-One relationship with Accounts)


## WordOfTheDay
- `name`
- `timestamp`

## WordHistory
- `name`
- `timestamp`

## Serializers

### AccountsSerializer

Serializes the `Accounts` model.

### SearchHistorySerializer

Serializes the `SearchHistory` model.

### UserSerializer

Serializes the `User` model.

### WordOfTheDaySerializer

Serializes the `WordOfTheDay` model.

### WordHistorySerializer

Serializes the `WordHistory` model.

## Usage

You can use the provided serializers in your Django REST Framework views to interact with the models. For example, you can use the `UserSerializer` to create, retrieve, update, and delete user records.

```python
# Example view using UserSerializer
from rest_framework import generics

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

## DB Stored Procs

# Word of the Day SQL Stored Procedures

This repository contains two SQL Server stored procedures for managing a "Word of the Day" feature on a website. The procedures are designed to select and insert the most searched word from the past week and to clear word search history older than one week.

## `generate_word_of_the_day`

This stored procedure is responsible for selecting the most searched word from the previous week and inserting it as the "Word of the Day" in the database.

### Parameters

- `@today_date`: DATE - The current date.
- `@last_week_start`: DATE - The start date of the previous week.
- `@last_week_end`: DATE - The end date of the previous week.
- `@most_searched_word`: NVARCHAR(255) - The most searched word to be determined by the procedure.

### Procedure Logic

1. Set `@today_date` to the current date.
2. Calculate `@last_week_start` and `@last_week_end` to define the previous week.
3. Use a common table expression (CTE) named `WordCounts` to count the occurrences of words in the `main_page_wordhistory` table from the previous week.
4. Select the top 1 most searched word from the CTE, ordered by word count in descending order.
5. Insert the selected word as the "Word of the Day" into the `main_page_wordoftheday` table, along with the current date.

## `clear_word_history_leave_only_last_week`

This stored procedure is responsible for clearing word search history records that are older than one week, helping to keep the database clean and maintain only recent search data.

### Procedure Logic

1. Disable the count of rows affected by the DELETE statement to improve performance (`SET NOCOUNT ON`).
2. Set `@OneWeekAgo` to a DATETIME value representing one week ago from the current date.
3. Delete records from the `main_page_wordhistory` table where the `timestamp` is earlier than `@OneWeekAgo`, effectively removing word search history older than one week.

## Usage

You can execute these stored procedures in your SQL Server environment to manage the "Word of the Day" feature and maintain a clean word search history.

Example usage for `generate_word_of_the_day`:

```sql
EXEC generate_word_of_the_day;

 