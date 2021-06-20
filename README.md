# Autoecole-app backend

This is the backend of Autoecole-App written in Python. It's purpose is to help instructors manage their driving school business.

## Installation

Create a virtual environment and nstall the package listed in requirements.txt

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Usage

1. Make migrations
```python
python3 manage.py makemigrations
```

2. Run migrations
```python
python3 manage.py migrate
```

3. Create superuser
```python
python3 manage.py createsuperuser
```

4. Run server
```python
python3 manage.py runserver
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)