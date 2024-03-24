# urls.py
from django.urls import path
from .views import upload_event, index, login_view, upload_study_material

urlpatterns = [
    path('upload_event/', upload_event),
    path("",index),
    path('login/', login_view),
    path('upload_study_material/', upload_study_material)
]
