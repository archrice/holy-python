from django.urls import path

from . import views

app_name = 'hp_app'
urlpatterns = [
            path('', views.index, name='index'),
            path('<int:question_id>/', views.detail, name='detail'),
            ]

