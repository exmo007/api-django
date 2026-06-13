from django.urls import path
from .views import sentry_test

urlpatterns = [
    path("sentry-test/", sentry_test),
]