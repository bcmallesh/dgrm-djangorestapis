from django.urls import path

from appointments.views import AppointmentView, SingleAppointmentView, MultipleAppointmentView

urlpatterns = [
    path('appointments/register/', AppointmentView.as_view()),
    path('appointments/edit/<int:pk>', SingleAppointmentView.as_view()),
    path('appointments/list/', MultipleAppointmentView.as_view()),
    path('appointments/view/<int:pk>', SingleAppointmentView.as_view()),
    path('appointments/delete/<int:pk>', SingleAppointmentView.as_view())
]