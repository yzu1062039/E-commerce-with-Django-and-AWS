# Django E-commerce Project

A simple E-commerce website built with Django.

## Features

- User authentication (Register, Login, Logout)
- Product catalog
- Shopping cart functionality
- Product categories
- Basic checkout process

## Setup Instructions

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run migrations:

```bash
python manage.py migrate
```

4. Create a superuser:

```bash
python manage.py createsuperuser
```

5. Run the development server:

```bash
python manage.py runserver
```

6. Visit http://127.0.0.1:8000/ in your browser

## Project Structure

- `store/` - Main application directory
  - `templates/` - HTML templates
  - `static/` - Static files (CSS, JS, images)
  - `models.py` - Database models
  - `views.py` - View functions
  - `urls.py` - URL configurations
