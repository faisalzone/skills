from django.urls import path
from .views import skill_view


app_name = 'skills'


urlpatterns = [
    path('', skill_view, name='my-skills'),
]