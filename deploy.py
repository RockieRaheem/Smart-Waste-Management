import os
import django
from django.core.management import execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
execute_from_command_line(['manage.py', 'migrate', '--noinput'])
os.system('gunicorn core.wsgi:application --bind 0.0.0.0:$PORT')