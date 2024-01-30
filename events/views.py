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
from .models import details

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
