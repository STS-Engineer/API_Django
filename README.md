# Django API Project

A Django REST API for managing user data with PostgreSQL database integration.

## Features

- **GET API**: Retrieve all users from the database
- **POST API**: Create new users in the database
- PostgreSQL connection with connection pooling
- JSON response format

## Installation

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure database connection in `pgapi/dbinfo/pgpool.py`

5. Run the Django development server:
```bash
cd pgapi
python manage.py runserver
```

## API Endpoints

### 1. GET Users - Retrieve All Users

**Endpoint:** `GET /dbinfo/tables/`

**Description:** Retrieves all users from the avo_users table.

**Response Example:**
```json
{
  "users": [
    {
      "id": 1,
      "user_name": "Rania Bakkali",
      "email": "rania.bakkali@avocarbon.com",
      "poste": "Machine Learning Engineer",
      "plant": "STS"
    },
    {
      "id": 2,
      "user_name": "Youssef Amrani",
      "email": "youssef.amrani@avocarbon.com",
      "poste": "AI Team Lead",
      "plant": "STS"
    }
  ]
}
```

**cURL Example:**
```bash
curl -X GET http://127.0.0.1:8000/dbinfo/tables/
```

### 2. POST Users - Create New User

**Endpoint:** `POST /dbinfo/users/`

**Description:** Creates a new user in the avo_users table.

**Request Body:**
```json
{
  "user_name": "John Doe",
  "email": "john.doe@avocarbon.com",
  "poste": "Software Developer",
  "plant": "STS"
}
```

**Response Example:**
```json
{
  "message": "User created successfully",
  "user": {
    "id": 4,
    "user_name": "John Doe",
    "email": "john.doe@avocarbon.com",
    "poste": "Software Developer",
    "plant": "STS"
  }
}
```

**cURL Example:**
```bash
curl -X POST http://127.0.0.1:8000/dbinfo/users/ \
  -H "Content-Type: application/json" \
  -d '{
    "user_name": "John Doe",
    "email": "john.doe@avocarbon.com",
    "poste": "Software Developer",
    "plant": "STS"
  }'
```

## Project Structure

```
pgapi/
├── manage.py
├── pgapi/
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── dbinfo/
    ├── views.py      # API endpoints
    ├── urls.py       # URL routing
    ├── pgpool.py     # Database connection
    └── ...
```

## Development

To run in development mode:

```bash
cd pgapi
python manage.py runserver
```
