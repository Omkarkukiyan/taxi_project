from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from geopy.geocoders import Nominatim 
from accounts.models import Account
from django.contrib import messages
from .models import Trip

@login_required(login_url='/')
def trip_details(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    if request.method == "POST":
        user = get_object_or_404(Account,id=request.user.id)
        pickup = request.POST['pickup']
        dropoff = request.POST['dropoff']
        STATUSES = 'REQUESTED'
        if request.method == "POST":
            trip_req = Trip.objects.create(rider=user,pickup=pickup, dropoff=dropoff,status=STATUSES)
            trip_req.save()
            messages.success(request, "Your request has been requested successfully")
            return redirect('rider_dashboard')
    else:
        return render(request, 'accounts/request.html',{'mapbox_access_token': mapbox_access_token })


def update_map(request):
    geolocator = Nominatim(user_agent="trip")
    if request.method == "POST":
        pickup = request.POST['pickup']
        dropoff = request.POST['dropoff']
        location1 = geolocator.geocode("pickup")
        location2 = geolocator.geocode("dropoff")

    return render(request,'accounts/request.html')    