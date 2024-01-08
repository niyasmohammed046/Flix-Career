from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='home'),
    path('Job_details/<int:id>/',views.job_detail,name='job_detail'),
]