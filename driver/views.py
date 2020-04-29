from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .forms import DriverRegisterForm
from accounts.models import Account
from trip.models import Trip
from driver.models import DriversAllTrips





def driver_signup(request):
    if request.method == "POST":
        form = DriverRegisterForm(request.POST,request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            license_id = form.cleaned_data.get('license_id')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            profile_pic = form.cleaned_data.get('profile_pic')
            is_driver = True
            user = Account.objects.create_user_for_driver(username=username, password1=password1,email=email, license_id=license_id, first_name=first_name, last_name=last_name,is_driver=is_driver,profile_pic=profile_pic)
            user.save()
            messages.success(request, "Your are now successfully registered")
            return redirect('driver_login') 
    else:
        form = DriverRegisterForm()    
    
    return render(request, 'driver/driver-signup.html', {'form':form})    
        

def driver_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request, "You are now logged in")
            return redirect('driver_dashboard')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('driver_login')
    else:            
        return render(request, 'driver/driver-login.html')
    

def driver_logout(request):
    auth.logout(request)
    messages.info(request, "You are now logged out")
    return redirect('driver_login')


@login_required(login_url='/')
def driver_dashboard(request):
    trips_requested = Trip.objects.filter(status='REQUESTED')
    trips_progress = Trip.objects.filter(status='IN_PROGRESS')
    trips_completed = DriversAllTrips.objects.filter(driver_email=request.user.email) 
    context = {
        'trips_requested': trips_requested,
        'trips_progress': trips_progress,
        'trips_completed': trips_completed
    }
    return render(request, 'driver/driver-dashboard.html', context)


def ride_request(request, trip_id):
    req = get_object_or_404(Trip, pk=trip_id)
    if req is not None:
        if req.status == "REQUESTED":
            Trip.objects.filter(trip_id = req.trip_id).update(status = "IN_PROGRESS") 
    return redirect('driver_dashboard')
    
def recent_trip(request, trip_id):
    driver_email = request.user.email
    driver_license_id = request.user.license_id
    recent = get_object_or_404(Trip, pk=trip_id)
    if recent is not None:
        if recent.status == "IN_PROGRESS":
            Trip.objects.filter(trip_id=recent.trip_id).update(status="COMPLETED")
        all_trips = DriversAllTrips.objects.create(driver_email=driver_email,rider_first_name=recent.rider.first_name,rider_last_name=recent.rider.last_name,rider_email=recent.rider.email,driver_license_id=driver_license_id,pickup=recent.pickup,dropoff=recent.dropoff,rider_profile_pic=recent.rider.profile_pic,status='COMPLETED')
        all_trips.save()
    return redirect('driver_dashboard')          

