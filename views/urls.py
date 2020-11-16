from django.urls import path
from views.views import Index
from views.views import getToken
from views.views import Regist
from views.views import Login
from views.views import PatientIndex
from views.views import Dignosis
from views.views import Appointment
from views.views import MakeAppointment
from views.views import DoctorIndex
from views.views import GetDiagnose
from views.views import UpateDiagnose

urlpatterns = [
    path('',Index.as_view()),
    path('get_token',getToken),
    path('check_user',Login.as_view()),
    path('add_user',Regist.as_view()),
    path('patient_info',PatientIndex.as_view()),
    path('diagnose_info',Dignosis.as_view()),
    path('get_patient',Appointment.as_view()),
    path('add_register',MakeAppointment.as_view()),
    path('doctor_index',DoctorIndex.as_view()),
    path('get_diagnose',GetDiagnose.as_view()),
    path('update_diagnose',UpateDiagnose.as_view())
]
