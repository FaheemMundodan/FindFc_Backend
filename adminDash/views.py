from django.http import JsonResponse
from .models import Event
from .models import StudyMaterial

from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from .models import Event
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def upload_event(request):
    if request.method == 'POST':
        # Get the form data
        title = request.POST.get('title')
        time = request.POST.get('time')
        venue = request.POST.get('venue')
        image = request.FILES.get('image')
        
        # Create Event object with form data
        event = Event.objects.create(title=title, time=time, venue=venue, image=image)
        
        return JsonResponse({'message': 'Event uploaded successfully', 'event_id': event.id})
    return JsonResponse({'error': 'Invalid request method'}, status=405)



def index(request):
    events = Event.objects.all()
    event_list = []

    for event in events:
        event_dict = {
            "venue": event.venue,
            "poster": event.image.url if event.image else None,
            "time": event.time,
            "date": event.date,
            "title": event.title  # Include the event title
        }

        print(event_dict)
        event_list.append(event_dict)

    return JsonResponse({"events": event_list})

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # Log in the user
            user_id = user.id  # Get the user ID
            return JsonResponse({"success": True, "message": "Login successful", "user_id": user_id, "redirect_url": "/"})
        else:
            return JsonResponse({"success": False, "message": "Invalid username or password"})
    return JsonResponse({"success": False, "message": "Invalid form data"})

@login_required
def logout_view(request):
    logout(request)  # Log out the user
    return JsonResponse({"success": True, "message": "Logout successful"})

@csrf_exempt
def upload_study_material(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        year = request.POST.get('year')
        material_type = request.POST.get('type')
        file = request.FILES.get('file')
        
        # Create StudyMaterial object with form data
        study_material = StudyMaterial.objects.create(
            category=category,
            year=year,
            material_type=material_type,
            file=file
        )
        
        return JsonResponse({'message': 'Study material uploaded successfully', 'material_id': study_material.id})
    return JsonResponse({'error': 'Invalid request method'}, status=405)