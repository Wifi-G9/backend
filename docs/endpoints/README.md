# Endpoints

# Top Instagram Posts

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

# ChatGPT descriptions

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

# PyTrends

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

# Popular Trends

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

# Sentiment Analysis

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

# Send a message to the developers

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

## Interest Over Time

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

## Search

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
