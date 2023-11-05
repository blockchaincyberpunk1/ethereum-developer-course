from django.urls import path
from . import views  # Note the use of dot (.) to indicate the current directory

urlpatterns = [
    path('', views.index, name='index'),
    # Define other URL patterns if needed
]
