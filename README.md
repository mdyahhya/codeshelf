# CodeShelf - Programming Learning Tracker

A simple web application to track programming languages and technologies I'm learning across Full Stack Development, Cyber Security, and Data Science.

## Features

- **CRUD Operations**: Create, Read, Update, Delete programming languages via REST API
- **External API Integration**: Import sample programming languages from GitHub's language data API
- **Dashboard**: Visual summary showing languages by category and proficiency level
- **REST API**: JSON API endpoints for all operations

## Tech Stack

- **Backend**: Python, Django, Django REST Framework
- **Database**: PostgreSQL (SQLite for local development)
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Render

## Local Setup

1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Create superuser: `python manage.py createsuperuser`
7. Run server: `python manage.py runserver`
8. Visit: http://127.0.0.1:8000/

## API Endpoints

- `GET /api/languages/` - List all languages
- `POST /api/languages/` - Create new language
- `GET /api/languages/<id>/` - Get specific language
- `PUT /api/languages/<id>/` - Update language
- `DELETE /api/languages/<id>/` - Delete language
- `GET /api/import-languages/` - Import from external API

## Admin Panel

Access Django admin at `/admin/` to manage data directly.

## External API

Uses GitHub's programming language colors API to fetch and import language data.
