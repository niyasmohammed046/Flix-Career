from django.urls import path
from . import views

urlpatterns = [
    path('upload/',views.upload,name="upload"),
    path('uploadfile/',views.uploadfile,name="uploadfile"),
]