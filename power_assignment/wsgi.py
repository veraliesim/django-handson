"""
WSGI config for grampower_assignment project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "grampower_assignment.settings")

application = get_wsgi_application()
try:
	from dj_static import Cling
	application = Cling(get_wsgi_application())
except:
	pass