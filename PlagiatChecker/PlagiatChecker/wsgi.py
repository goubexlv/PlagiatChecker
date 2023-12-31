import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PlagiatChecker.settings')

application = get_wsgi_application()
