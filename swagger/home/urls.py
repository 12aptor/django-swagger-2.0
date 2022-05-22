


from django.urls import path
from . import views


urlpatterns = [
    path('casas/', views.HomeView.as_view()),
]