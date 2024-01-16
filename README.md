# Trendifyr - Backend Documentation

##  1. <a name='Overview'></a>Overview

This is the backend repository for the Trendifyr web application. This project is written in Django.

##  2. <a name='TableofContents'></a>Table of Contents

- [Trendifyr - Backend Documentation](#trendifyr---backend-documentation)
  - [1. Overview](#1-overview)
  - [2. Table of Contents](#2-table-of-contents)
  - [3. Installation](#3-installation)
  - [4. Project Structure](#4-project-structure)
  - [5. API Endpoints](#5-api-endpoints)
    - [5.1. Top Instagram Posts](#51-top-instagram-posts)
    - [5.2. ChatGPT descriptions](#52-chatgpt-descriptions)
    - [5.3. PyTrends](#53-pytrends)
    - [5.4. Popular Trends](#54-popular-trends)
    - [5.5. Sentiment Analysis](#55-sentiment-analysis)
    - [5.6. Send a message to the developers](#56-send-a-message-to-the-developers)
    - [5.7. Interest Over Time](#57-interest-over-time)
    - [5.8. Search](#58-search)
    - [5.9. Sign Up](#59-sign-up)
    - [5.10. Log In](#510-log-in)
    - [5.11. Image Description API](#511-image-description-api)
    - [5.12. Photo description to post description](#512-photo-description-to-post-description)
    - [5.13. Photo description to Deezer song](#513-photo-description-to-deezer-song)
    - [5.14. Engagement rate](#514-engagement-rate)
  - [6. Database Models](#6-database-models)
    - [6.1. Accounts](#61-accounts)
    - [6.2. DeveloperMessage](#62-developermessage)
    - [6.3. SearchHistory](#63-searchhistory)
    - [6.4. User](#64-user)
    - [6.5. WordOfTheDay](#65-wordoftheday)
    - [6.6. WordHistory](#66-wordhistory)
    - [6.7. Serializers](#67-serializers)
    - [6.8. Usage](#68-usage)
    - [6.9. DB Stored Procs](#69-db-stored-procs)
      - [6.9.1. Word of the Day SQL Stored Procedures](#691-word-of-the-day-sql-stored-procedures)
      - [6.9.2. Usage](#692-usage)
  - [7. Authentication](#7-authentication)
  - [8. Dependencies](#8-dependencies)
    - [8.1. Installation Guide](#81-installation-guide)
      - [8.1.1. Install the Microsoft ODBC driver for SQL Server (Linux)](#811-install-the-microsoft-odbc-driver-for-sql-server-linux)
      - [8.1.2. Install the Microsoft ODBC driver for SQL Server (Windows)](#812-install-the-microsoft-odbc-driver-for-sql-server-windows)
  - [9. Coding Standards](#9-coding-standards)
  - [10. Contributing](#10-contributing)
    - [10.1. Django View Template](#101-django-view-template)
    - [10.2. Usage](#102-usage)

##  3. <a name='Installation'></a>Installation

This project requires installation of multiple `pip` packages, which is why we recommend setting up a virtual environment before running it.

```bash
# Clone the repository
git clone https://github.com/Wifi-G9/backend.git

# Change into the project directory
cd backend/

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install dependencies
python3 -m pip install -r dependencies/packages.txt

# Start the server
python manage.py runserver
```

##  4. <a name='ProjectStructure'></a>Project Structure
```
backend/
|-- backend/ <- This should be the root directory
|   |-- dependencies/
|   |
|   |-- main_page/
|   |   |-- __init__.py
|   |
|   |-- tsma/
|   |   |-- __init__.py
|   |
|   |-- user_page/
|   |   |-- __init__.py
|   |
|   |-- manage.py
```

##  5. <a name='APIEndpoints'></a>API Endpoints
###  5.1. <a name='TopInstagramPosts'></a>Top Instagram Posts

* **Endpoint:** `/search-instagram`
* **Method:** GET
* **Request body:** JSON object with the following fields:
    * `query`: The search term for the search functionality with Instagram posts.

* **Response body:** JSON array with the following fields for each post:
    * `link`: The URL of the original Instagram post.
    * `description`: The caption of the Instagram post.
    * `sentiment_analysis`: A JSON object with the following fields:
        * `sentiment`: The sentiment of the post's description, either "positive", "negative", or "neutral".
        * `score`: A score indicating the strength of the sentiment.
    * `likes`: The number of likes on the Instagram post.
    * `comments`: The number of comments on the Instagram post.
    * `hashtags`: An array of hashtags used in the Instagram post's description.
    * `engagement_score`: A calculated score based on the number of likes and comments on the post.
    * `image_description`: A description of the image in the Instagram post, generated using image recognition techniques.

* **Example request:**

```json
{
"query": "artificial intelligence"
}
```

* **Example response:**

```json
{
  "posts-list": [
    {
      "link": "https://www.instagram.com/p/CWO6hY_j_rX/",
      "description": "AI is the future!",
      "sentiment_analysis": {
        "sentiment": "positive",
        "score": 0.9
      },
      "likes": 1000,
      "comments": 500,
      "hashtags": [
        "#AI",
        "#artificialintelligence",
        "#future"
      ],
      "engagement_score": 1500,
      "image_description": "A person using a computer with a futuristic interface."
    },
    {
      "link": "https://www.instagram.com/p/CWQ3456j_rX/",
      "description": "AI is changing the world.",
      "sentiment_analysis": {
        "sentiment": "positive",
        "score": 0.8
      },
      "likes": 800,
      "comments": 400,
      "hashtags": [
        "#AI",
        "#artificialintelligence",
        "#change"
      ],
      "engagement_score": 1200,
      "image_description": "A group of robots working together in a factory."
    },
    {
      "link": "https://www.instagram.com/p/CWO6789j_rX/",
      "description": "AI is amazing!",
      "sentiment_analysis": {
        "sentiment": "positive",
        "score": 1.0
      },
      "likes": 600,
      "comments": 300,
      "hashtags": [
        "#AI",
        "#artificialintelligence",
        "#amazing"
      ],
      "engagement_score": 900,
      "image_description": "A child playing with an AI-powered robot."
    }
  ]
}
```

###  5.2. <a name='ChatGPTdescriptions'></a>ChatGPT descriptions

* **Endpoint:** `/describe`
* **Method:** POST
* **Request body:** JSON object with the following fields:
    * `message`: A string with a word or phrase that will be described by ChatGPT.

* **Response body:** JSON object with the following fields:
    * `description`: The description of the word/phrase that was sent.

**Example request:**

```
POST /chat HTTP/1.1
Content-Type: application/json

{
  "message": "Black coffee"
}
```

**Example response:**

```json
{
  "response": "Black coffee is a simple beverage made by brewing coffee beans without the addition of milk, cream, or sugar. It retains the pure, robust flavor of the coffee beans."
}
```

###  5.3. <a name='PyTrends'></a>PyTrends

* **Endpoint:** `/similar-trends`
* **Method:** GET
* **Request body:** JSON object with the following fields:
    * `query`: A string with a word or phrase.

* **Response body:** JSON object with the following fields:
    * `trends`: An array of trending topics, each of which is a JSON object with the following fields:
        * `name`: The name of the trending topic.
        * `score`: A score indicating how trending the topic is.

**Example response:**

```json
{
  "trends": [
        {
          "name": "machine learning",
          "score": 95
        },
        {
          "name": "deep learning",
          "score": 90
        },
        {
          "name": "natural language processing",
          "score": 85
        },
        {
          "name": "computer vision",
          "score": 80
        },
        {
          "name": "robotics",
          "score": 75
        }
  ]
}

```

###  5.4. <a name='PopularTrends'></a>Popular Trends

* **Endpoint:** `/popular-trends`
* **Method:** GET
* **Request body:** JSON object with the following fields:
    * `count`: Number that represents the amount of trends to be returned.

* **Response body:** JSON array with the following fields for each trend:
    * `title`: The title of the trend.
    * `description`: A brief description of the trend.

* **Example response:**

```json
{
  "trends": [
    {
      "title": "Artificial Intelligence",
      "description": "The development of intelligent agents, which are systems that can reason, learn, and act autonomously."
    },
    {
      "title": "Metaverse",
      "description": "A hypothetical iteration of the Internet as a single, universal and immersive virtual world that is facilitated by the use of virtual reality and augmented reality headsets."
    },
    {
      "title": "Climate Change",
      "description": "Long-term shifts in temperatures and weather patterns, mainly caused by human activities, especially the burning of fossil fuels."
    },
    {
      "title": "Cryptocurrency",
      "description": "A digital or virtual currency that uses cryptography for security. It is decentralized, meaning it is not subject to government or financial institution control."
    },
    {
      "title": "Electric Vehicles",
      "description": "Electric vehicles (EVs) are cars, trucks, buses, and motorcycles that run on electricity instead of gasoline or diesel."
    },
    {
      "title": "Sustainable Fashion",
      "description": "Sustainable fashion is a movement and process that encourages the fashion industry to become more sustainable in terms of environmental impact, social impact, and economic impact."
    },
    {
      "title": "Remote Work",
      "description": "Remote work, also known as telework or telecommuting, is the practice of working away from a central office and using telecommunications technology to stay connected to the workplace."
    }
  ]
}
```

###  5.5. <a name='SentimentAnalysis'></a>Sentiment Analysis

* **Endpoint:** `/sentiment-analysis`
* **Method:** POST
* **Request body:** JSON object with the following fields:
    * `text`: The text to be analyzed.

* **Response body:** JSON object with the following fields:
    * `sentiment`: The sentiment of the text, either "positive", "negative", or "neutral".
    * `score`: A score indicating the strength of the sentiment.

* **Example request:**
```json
{
"text": "This is a positive sentiment."
}
```

* **Example response:**
```json
{
"sentiment": "positive",
"score": 0.8
}

```

###  5.6. <a name='Sendamessagetothedevelopers'></a>Send a message to the developers

* **Endpoint:** `/developer-message`
* **Method:** POST
* **Request body:** JSON object with the following fields:
    * `message`: The text to be analyzed.

* **Response body:** None

* **Example request:**
```json
{
"text": "This app is really cool."
}
```

###  5.7. <a name='InterestOverTime'></a>Interest Over Time

* **Endpoint:** `/interest-over-time`
* **Method:** GET
* **Request body:** JSON object with the following fields:
    * `query`: The search term to track interest over time.
    * `start_date`: The start date for the interest data, in YYYY-MM-DD format.
    * `end_date`: The end date for the interest data, in YYYY-MM-DD format.

* **Response body:** JSON array with the following fields for each data point:
    * `date`: The date for the interest data point, in YYYY-MM-DD format.
    * `interest`: The interest score for the search term on that date, where 100 represents the peak interest.

* **Example request:**

```
GET /interest-over-time HTTP/1.1
Content-Type: application/json

{
"query": "artificial intelligence",
"start_date": "2020-01-01",
"end_date": "2023-11-11"
}
```

* **Example response:**

```json
{
  "interest": [
    {
      "date": "2020-01-01",
      "interest": 20
    },
    {
      "date": "2020-02-01",
      "interest": 30
    },
    {
      "date": "2020-03-01",
      "interest": 40
    },
    {
      "date": "2020-04-01",
      "interest": 50
    },
    {
      "date": "2020-05-01",
      "interest": 60
    },
    {
      "date": "2020-06-01",
      "interest": 70
    },
    {
      "date": "2020-07-01",
      "interest": 80
    },
    {
      "date": "2020-08-01",
      "interest": 90
    },
    {
      "date": "2020-09-01",
      "interest": 100
    },
    {
      "date": "2020-10-01",
      "interest": 95
    },
    {
      "date": "2020-11-01",
      "interest": 90
    },
    {
      "date": "2020-12-01",
      "interest": 85
    },
    {
      "date": "2021-01-01",
      "interest": 80
    },
    {
      "date": "2021-02-01",
      "interest": 75
    },
    {
      "date": "2021-03-01",
      "interest": 70
    },
    {
      "date": "2021-04-01",
      "interest": 65
    },
    {
      "date": "2021-05-01",
      "interest": 60
    },
    {
      "date": "2021-06-01",
      "interest": 55
    },
    {
      "date": "2021-07-01",
      "interest": 50
    },
    {
      "date": "2021-08-01",
      "interest": 45
    },
    {
      "date": "2021-09-01",
      "interest": 40
    },
    {
      "date": "2021-10-01",
      "interest": 35
    },
    {
      "date": "2021-11-01",
      "interest": 30
    },
    {
      "date": "2021-12-01",
      "interest": 25
    },
    {
      "date": "2022-01-01",
      "interest": 20
    },
    {
      "date": "2022-02-01",
      "interest": 15
    }
  ]
}
```

###  5.8. <a name='Search'></a>Search

* **Endpoint:** `/search`
* **Method:** GET
* **Request body:** JSON object with the following fields:
    * `query`: The search term add to word of the day statistic.

* **Response body:** 404 if the word does not belong to the dictionary, 200 if the search is valid

* **Example request:**

```
GET /search HTTP/1.1
Content-Type: application/json

{
"query": "artificial intelligence",
}
```

###  5.9. <a name='SignUp'></a>Sign Up

* **Endpoint:** `/signup`

* **Method:** POST
* **Request body:**
    * `email:` The email that the user provided
    * `username:` The username provided by the user
    * `password:` The password provided by the user
    * `verify_password:` Password confirmation
* **Response body:**
    * `message`: User registration successful.
* **Response body:** 404 if the user exists, 200 if the signup is valid
* **Example request:**

```json
{
  "email": "user@example.com",
  "username": "example_user",
  "password": "securepassword123",
  "verify_password": "securepassword123"
}
```

* **Example response:**
```json
{
  "message": "Sign-up successful"
}
```

###  5.10. <a name='LogIn'></a>Log In

* **Endpoint:** `/login`

* **Method:** POST
* **Request body:**
    * `email:` The email that the user provided
    * `password:` The password provided by the user
* **Request body:**
    * `message`: User login successful.
* **Response body:** 404 if the user exists, 200 if the signup is valid
* **Example request:**

```json
{
  "email": "user@example.com",
  "password": "securepassword123"
}
```

* **Example response:**
```json
{
  "message": "Sign-up successful"
}
```

###  5.11. <a name='ImageDescriptionAPI'></a>Image Description API

**Endpoint:** `/<username>/describe-photo`
* **Method:** POST
* **Request body:**
    * `photo:` Base64-encoded image data
* **Request body:**
    * `description:` Extracted text description of the image
* **Request Body:** 200 if the result is correct, 404 if there was an error

* **Example request:**
```json
{
  "photo": "<Base64-encoded image data>"
}
```
* **Example Response:**
```json
{
  "description": "<Extracted text description of the image>"
}
```

###  5.12. <a name='Photodescriptiontopostdescription'></a>Photo description to post description

**Endpoint:** `/<username>/photo-desc-post-desc`
* **Method:** POST
* **Request body:**
    * `description:` Text message from Google photos
* **Request body:**
    * `description:` Description message to put on the post description
* **Request Body:** 200 if the result is correct, 404 if there was an error

* **Example request:**
```json
{
  "description": "Dog running after a ball"
}
```
* **Example Response:**
```json
{
  "description": "Chasing dreams and balls 🐾🎾 Our furry friend in action, embracing the joy of the great outdoors. Every sprint, every leap is a reminder to live life with boundless enthusiasm. 🌳🌞 #DogLife #BallChaser #FurryAdventures"
}
```

###  5.13. <a name='PhotodescriptiontoDeezersong'></a>Photo description to Deezer song

**Endpoint:** `/<username>/description-deezer`
**Method:** POST
* **Request body:**
    * `description:` Text message from Google photos
* **Request body:**
    * `link:` Text with link for a song that matches the description
* **Request Body:** 200 if the result is correct, 404 if there was an error

* **Example request:**
```json
{
  "photo": "Dog running after a ball"
}
```
* **Example Response:**
```json
{
  "link": "https://www.deezer.com/en/track/83890415"
}
```

###  5.14. <a name='Engagementrate'></a>Engagement rate

**Endpoint:** `/<username>/engagement-score`
**Method:** POST
* **Request body:**
    * `user_id:` The instagram id for the user
* **Request body:**
    * `score:` Number representing the user engagement score
* **Request Body:** 200 if the result is correct, 404 if there was an error

* **Example Request:**
```json
{
  "user_id": "908409827482750854725"
}
```
* **Example Response:**
```json
{
  "score": 94
}
```

##  6. <a name='DatabaseModels'></a>Database Models
###  6.1. <a name='Accounts'></a>Accounts

- `instagram_access_token`
- `twitter_access_token`
- `facebook_access_token`

###  6.2. <a name='DeveloperMessage'></a>DeveloperMessage

- `message`
- `timestamp`
- `user` (Foreign Key to User)

###  6.3. <a name='SearchHistory'></a>SearchHistory

- `user` (Foreign Key to User)
- `timestamp`
- `search_query`

###  6.4. <a name='User'></a>User

- `name`
- `age`
- `email`
- `password`
- `accounts` (One-to-One relationship with Accounts)


###  6.5. <a name='WordOfTheDay'></a>WordOfTheDay
- `name`
- `timestamp`

###  6.6. <a name='WordHistory'></a>WordHistory
- `name`
- `timestamp`

###  6.7. <a name='Serializers'></a>Serializers
- AccountsSerializer
- SearchHistorySerializer
- UserSerializer
- WordOfTheDaySerializer
- WordHistorySerializer

###  6.8. <a name='Usage'></a>Usage

You can use the provided serializers in your Django REST Framework views to interact with the models. For example, you can use the `UserSerializer` to create, retrieve, update, and delete user records.

```python
# Example view using UserSerializer
from rest_framework import generics

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

###  6.9. <a name='DBStoredProcs'></a>DB Stored Procs

####  6.9.1. <a name='WordoftheDaySQLStoredProcedures'></a>Word of the Day SQL Stored Procedures

This repository contains two SQL Server stored procedures for managing a "Word of the Day" feature on a website. The procedures are designed to select and insert the most searched word from the past week and to clear word search history older than one week.

- `generate_word_of_the_day`: This stored procedure is responsible for selecting the most searched word from the previous week and inserting it as the "Word of the Day" in the database.
  - Parameters:
    - `@today_date`: DATE - The current date.
    - `@last_week_start`: DATE - The start date of the previous week.
    - `@last_week_end`: DATE - The end date of the previous week.
    - `@most_searched_word`: NVARCHAR(255) - The most searched word to be determined by the procedure.
  - Procedure Logic:
    - Set `@today_date` to the current date.
    - Calculate `@last_week_start` and `@last_week_end` to define the previous week.
    - Use a common table expression (CTE) named `WordCounts` to count the occurrences of words in the `main_page_wordhistory` table from the previous week.
    - Select the top 1 most searched word from the CTE, ordered by word count in descending order.
    - Insert the selected word as the "Word of the Day" into the `main_page_wordoftheday` table, along with the current date.

- `clear_word_history_leave_only_last_week`: This stored procedure is responsible for clearing word search history records that are older than one week, helping to keep the database clean and maintain only recent search data.
  - Procedure Logic:
    - Disable the count of rows affected by the DELETE statement to improve performance (`SET NOCOUNT ON`).
    - Set `@OneWeekAgo` to a DATETIME value representing one week ago from the current date.
    - Delete records from the `main_page_wordhistory` table where the `timestamp` is earlier than `@OneWeekAgo`, effectively removing word search history older than one week.

####  6.9.2. <a name='Usage-1'></a>Usage

You can execute these stored procedures in your SQL Server environment to manage the "Word of the Day" feature and maintain a clean word search history.

Example usage for `generate_word_of_the_day`:

```sql
EXEC generate_word_of_the_day;
```

We also have Factories for generating mock data:
- UserFactory
- AccountsFactory
- DeveloperMessageFactory
- SearchHistoryFactory
- WordHistoryFactory
- WordOfTheDayFactory

##  7. <a name='Authentication'></a>Authentication
You will need to setup your `.env` file with the following credentials (actual values removed for confidentiality):
```
# Database connection string
DB_ENGINE=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

# Team gmail account
EMAIL=
PASSWORD=

# Meta developer stuff
RAPID_API_KEY=
RAPIDAPI_KEY=
RAPIDAPI_HOST_INFO=
RAPIDAPI_HOST_FEED=

# OpenAI key
OPENAI_KEY=
```
##  8. <a name='Dependencies'></a>Dependencies
To connect to the database, you will need the specific database drivers.

###  8.1. <a name='InstallationGuide'></a>Installation Guide
####  8.1.1. <a name='InstalltheMicrosoftODBCdriverforSQLServerLinux'></a>Install the Microsoft ODBC driver for SQL Server (Linux)

1. Create a `file.sh` with the following code:

    ```bash
    #!/bin/bash

    if ! [[ "18.04 20.04 22.04 23.04" == *"$(lsb_release -rs)"* ]];
    then
        echo "Ubuntu $(lsb_release -rs) is not currently supported.";
        exit;
    fi

    curl https://packages.microsoft.com/keys/microsoft.asc | sudo tee /etc/apt/trusted.gpg.d/microsoft.asc

    curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list | sudo tee /etc/apt/sources.list.d/mssql-release.list

    sudo apt-get update

    # optional: for bcp and sqlcmd
    sudo ACCEPT_EULA=Y apt-get install -y msodbcsql18
    sudo ACCEPT_EULA=Y apt-get install -y mssql-tools18
    echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc
    source ~/.bashrc

    # optional: for unixODBC development headers
    sudo apt-get install -y unixodbc-dev
    ```

2. Give the file permission to execute:
   ```bash
   chmod 700 file.sh
   ```
3. Run the script:
   ```bash
   sudo ./file.sh
   ```

####  8.1.2. <a name='InstalltheMicrosoftODBCdriverforSQLServerWindows'></a>Install the Microsoft ODBC driver for SQL Server (Windows)
Click on the desired link to get the installer:
- [Download Microsoft ODBC Driver 18 for SQL Server (x64)](https://go.microsoft.com/fwlink/?linkid=2249006)
   or
- [Download Microsoft ODBC Driver 18 for SQL Server (x86)](https://go.microsoft.com/fwlink/?linkid=2249005)

##  9. <a name='CodingStandards'></a>Coding Standards
- File names: lowercase snake_case (e.g. my_function())
- Class names: uppercase camelCase (e.g. MyClass)
- Global variables: uppercase snake_case (e.g. Global_var)
- Instance variables: lowercase snake_case, protected variables begin with an underscore, and private variables begin with two underscores (e.g. public_var, _protected_var, __private_var)
- Methods, functions: lowercase snake_case (e.g. my_function())
- Constants: uppercase snake_case (e.g. MY_CONSTANT)

##  10. <a name='Contributing'></a>Contributing
***Do not change `.gitignore` file***
***Do not modify the current directory tree structure***

###  10.1. <a name='DjangoViewTemplate'></a>Django View Template
```python
# needed imports
<import requests>
from django.views import View
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

# constants/static variables
API_<NAME> = <"https://api.site.com/api/v2">


class <Name>(View):
    # if you need some initializations go head but there is no need
    # get method with request as a required parameter
    # if you don't use self just write:
    # @staticmethod
    def get(self, request: Request, <other_parameter>: <type>) -> Response:
    """
    <Describe the function here>
    :param request: Request
    <:param other_parameter: type and a description if needed>
    :return: Response with the data: <type> and status: status
    <Describe the Response, e.g.:>
    <Response(
        {
            key: value if value exists else other_value
        },
        status_code: type = 200 if value exists else 404
    )>
    """
        # if you want to call want to call the WordSearch class check the code below
        # how to get the query params
        <query_param> = request.query_params.get(<name_of_query_param>, None)

        # the rest is your choice just be careful how you send back the information, e.g.:
        return Response(data=<{ key: value, }>, status=status.<HTTP_200_OK>)
```

The WordSearch class view can be use by everyone to get:
1. The `word of the day` if there is nothing in the search bar, with the `status_code 200`
2. The `searched word` if there is something in the search bar, with the `status_code 200`
3. `"Not found"` response if the word doesn't exist, with the `status_code 404`

###  10.2. <a name='Usage-1'></a>Usage
```python
word_searched: Response = WordSearch.as_view()(request)

if word_searched.status_code == 404:
    return word_searched

# do whatever you want with word_searched.data
word = word_searched.data
# word will now have the dictionary of the response data
```
