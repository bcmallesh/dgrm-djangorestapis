from django.urls import path

from patients.views import PatientView, SingleUserView, MultipleUserView

urlpatterns = [
    path('patients/register/', PatientView.as_view()),
    path('patients/edit/<int:pk>', SingleUserView.as_view()),
    path('patients/list/', MultipleUserView.as_view()),
    path('patients/view/<int:pk>', SingleUserView.as_view())
]