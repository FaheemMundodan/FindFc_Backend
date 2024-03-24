# from django.urls import path
# from . import views
# urlpatterns= [
#     path("",views.index)
# ]
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index),
    path("materials/",views.materials_list),
    path('upload/material/', views.upload_material, name='upload_material'),
    path('upload/gallery/', views.upload_gallery, name='upload_gallery'),
    # Other URLs...
    # path('materials', views.materials, name='study materials'),
    # ... your other url patterns
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
