release: python manage.py migrate
web: python manage.py collectstatic --no-input; gunicorn django_store.wsgi --log-file - --log-level debug
