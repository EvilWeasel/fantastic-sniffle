from django.urls import path
from .views import FragebogenHome


urlpatterns = [
    path('', FragebogenHome.as_view(), name='fragebogen_start'),
]