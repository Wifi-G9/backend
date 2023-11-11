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
