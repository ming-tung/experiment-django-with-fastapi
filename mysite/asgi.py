"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

import django
from fastapi import FastAPI

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

django.setup(set_prefix=False)

from poll.routers import books_router  # noqa: E402

application = FastAPI()
application.include_router(books_router, tags=["books"], prefix="/api/books")
