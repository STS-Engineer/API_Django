from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .pgpool import pool

def list_tables(request):
    with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, user_name, email, poste, plant
                FROM avo_users
            """)
            # Get column names
            columns = [desc[0] for desc in cur.description]
            # Get all rows and convert to list of dictionaries
            users = []
            for row in cur.fetchall():
                user_dict = dict(zip(columns, row))
                users.append(user_dict)
    return JsonResponse({'users': users})


@csrf_exempt
@require_http_methods(["POST"])
def create_user(request):
    try:
        # Parse JSON data from request body
        data = json.loads(request.body)

        # Validate required fields
        required_fields = ['user_name', 'email', 'poste', 'plant']
        for field in required_fields:
            if field not in data:
                return JsonResponse({
                    'error': f'Missing required field: {field}'
                }, status=400)

        # Extract data
        user_name = data['user_name']
        email = data['email']
        poste = data['poste']
        plant = data['plant']

        # Insert new user into database
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO avo_users (user_name, email, poste, plant)
                    VALUES (%s, %s, %s, %s)
                    RETURNING id, user_name, email, poste, plant
                """, (user_name, email, poste, plant))

                # Get the inserted user data
                new_user = cur.fetchone()
                columns = [desc[0] for desc in cur.description]
                user_dict = dict(zip(columns, new_user))

                # Commit the transaction
                conn.commit()

        return JsonResponse({
            'message': 'User created successfully',
            'user': user_dict
        }, status=201)

    except json.JSONDecodeError:
        return JsonResponse({
            'error': 'Invalid JSON data'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'error': f'Database error: {str(e)}'
        }, status=500)
