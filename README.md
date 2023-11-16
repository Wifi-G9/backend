# Backend

###

| ❗ This is very important ❗ |
|----------------------------|

---

### ***Keep the `.env` file confidential***

### ***Everything related to connections, accounts and access tokens should be written in `.env`***

### ***Do not change `.gitignore` file***

### ***Do not add unnecessary file***

### ***Write documentation about your Response data from your view***

### ***Location of the current working directory should look like***

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

---

## How to install dependencies

### 1. Create a virtual environment:

```bash
python -m venv venv
```

### 2. Activate the environment:

#### Linux

```bash
source venv/bin/activate
```

#### Windows

```shell
venv\Scripts\activate
```

### 3. Enter the dependencies file:

```bash
cd dependencies
```

### 4. Run dependencies:

#### Linux

```bash
./install_script.sh
```

#### Windows

```shell
.\install_script.bat
```

---

## [Here you can see how to install the database drivers](docs/DB_README.md "Install DB drivers")

---

## How to make a view in Django
###### This is just an example no need to have everything you see
###### Everything that is put between "<>" is a placeholder or optional
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

---

## The WordSearch class view can be use by everyone to get:
### 1. The `word of the day` if there is nothing in the search bar, with the `status_code 200`
### 2. The `searched word` if there is something in the search bar, with the `status_code 200`
### 3. `"Not found"` response if the word doesn't exist, with the `status_code 404`
## Usage
```python
word_searched: Response = WordSearch.as_view()(request)

if word_searched.status_code == 404:
    return word_searched

# do whatever you want with word_searched.data
word = word_searched.data
# word will now have the dictionary of the response data
```