from django.urls import path
from views.views import Index

urlpatterns = [
    path('',Index.as_view()),
    # path('get_token',getToken),
    # path('check_user',Login.as_view()),
    # path('add_user',Regist.as_view()),
    # path('patient_info',PatientIndex.as_view()),
    # path('diagnose_info',Dignosis.as_view()),
    # path('get_patient',Appointment.as_view()),
]
