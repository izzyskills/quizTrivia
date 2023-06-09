from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logoutUser, name="logout"),
    path("", views.home_view, name="home"),
    path("profile/", views.dashboard_view, name="dashboard"),
    path("quiz/select/", views.select_quiz_view, name="quiz_select"),
    path("submit/new-quiz", views.submit_new_quiz_view, name="new_quiz"),
    path("quiz/info/<str:pk>/", views.pre_quiz_view, name="pre_quiz"),
    path("quiz/<str:pk>/start/<int:session_id>/", views.quiz_view, name="quiz_start"),
    path("quiz/previous/", views.previous_quiz_view, name="previous_quiz"),
    path("quiz/previous/review/<str:pk>/", views.review_quiz_view, name="review"),
]
