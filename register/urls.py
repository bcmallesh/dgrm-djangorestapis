from django.urls import path

from register.views import RegisterView, SignView, SingleUserView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('signin/', SignView.as_view()),
    path('editprofile/<int:pk>', SingleUserView.as_view()),
    path('viewprofile/<int:pk>', SingleUserView.as_view())
]