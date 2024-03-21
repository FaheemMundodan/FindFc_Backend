# from django.http import JsonResponse
# from .models import details

# def index(request):
#     # Fetch all event details from the database
#     events = details.objects.all().values()
#     # Convert the queryset to a list of dictionaries
#     event_list = list(events)
#     print((event_list[0]['poster']))
#     # Return a JsonResponse containing the event data
#     return JsonResponse({"events": event_list})

from django.http import JsonResponse
from django.conf import settings
from .models import details,Material,gallery
from django.core import serializers



def index(request):
     events = details.objects.all()
     event_list = []

     for event in events:
         event_dict = {
             "time": event.time,
             "venue": event.venue,
             "poster": event.poster.url if event.poster else None
         }
         event_list.append(event_dict)

     return JsonResponse({"events": event_list})


from django.http import JsonResponse
from .models import Material

# def materials_list(request):
#     course = request.GET.get('course')
#     year = request.GET.get('year')
#     material_type = request.GET.get('material_type')

#     materials = Material.objects.filter(
#         course__icontains=course if course else "",
#         year__icontains=year if year else "",
#         material_type__icontains=material_type if material_type else "",
#     ).values('id', 'file', 'course', 'year', 'material_type')  # Adjust the fields as necessary

#     materials_list = list(materials)
#     return JsonResponse({"materials": materials_list})

from django.http import JsonResponse
from django.conf import settings
from .models import Material

def materials_list(request):
    course = request.GET.get('course')
    year = request.GET.get('year')
    material_type = request.GET.get('material_type')

    materials = Material.objects.filter(
        course__icontains=course if course else "",
        year__icontains=year if year else "",
        material_type__icontains=material_type if material_type else "",
    )

    # Prepare a list of materials with downloadable URLs
    materials_list = [{
        'id': material.id,
        'file': request.build_absolute_uri(material.file.url) if material.file else None,
        'course': material.course,
        'year': material.year,
        'material_type': material.material_type
    } for material in materials]

    return JsonResponse({"materials": materials_list})

def index(request):
     events = gallery.objects.all()
     event_list = []

     for event in events:
         event_dict = {
            
             "venue": event.event_name,
             "poster": event.poster.url if event.poster else None
         }
         event_list.append(event_dict)

     return JsonResponse({"events": event_list})