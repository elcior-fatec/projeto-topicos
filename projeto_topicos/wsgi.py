"""
WSGI config for projeto_topicos project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto_topicos.settings')

application = Cling(get_wsgi_application())

