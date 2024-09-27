from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import UserProfile, Doctor, Appointment
from .forms import UserProfileForm, AppointmentForm

def profile_view(request):
    return render(request, 'profile.html', {'profile': profile})

# New view for the homepage
def home_view(request):
    return HttpResponse("Welcome to HealthConnect!")
def update_profile_view(request):
    profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'update_profile.html', {'form': form})

def doctors_list_view(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors_list.html', {'doctors': doctors})

def book_appointment_view(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = UserProfile.objects.get(user=request.user)
            appointment.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'book_appointment.html', {'form': form})

def appointment_list_view(request):
    appointments = Appointment.objects.filter(user__user=request.user)
    return render(request, 'appointment_list.html', {'appointments': appointments})