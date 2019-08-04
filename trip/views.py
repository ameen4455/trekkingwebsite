from django.shortcuts import render

# Create your views here.
from .models import Places,District

def home(request):
    district = District.objects.all()
    context = {
        'district': district,
        'places': Places.objects.all()
    }
    return render(request,"home.html", context)

def item(request):
    id = request.GET['select2'] 
    context = {
         'item': Places.objects.get(id=id),

    }
    return render(request, "item.html", context)
