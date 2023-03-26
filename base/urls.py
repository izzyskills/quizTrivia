from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('', views.home_view, name='home'),
    path('profile/', views.dashboard_view, name='dashboard'),
    path('exam/select/', views.select_exam_view, name='exam_select'),
    path('submit/new-quiz', views.submit_new_quiz_view, name="new_quiz"),
]
