import os
import sys
from django.core.management import execute_from_command_line

# Run migrations
execute_from_command_line(['manage.py', 'migrate', '--noinput'])

# Start Gunicorn
os.system('gunicorn core.wsgi:application --bind 0.0.0.0:$PORT')