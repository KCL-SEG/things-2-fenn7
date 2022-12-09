from django.shortcuts import render
from .models import Thing
from .forms import ThingForm

def home(request):
    if request.method == "POST":
        form = ThingForm(request.POST)
        if form.is_valid():
            return render(request, 'home.html', {'form': form})
    form = StudentSignUpForm()
    return render(request, "home.html", {"form": form})
    
