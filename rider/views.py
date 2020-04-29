from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.contrib.auth.models import User 
from .forms import RiderRegisterForm
from accounts.models import Account
from trip.models import Trip





def rider_signup(request):
    if request.method == "POST":
        form = RiderRegisterForm(request.POST,request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            profile_pic = form.cleaned_data.get('profile_pic')
            is_rider=True
            user = Account.objects.create_user_for_rider(username=username, password1=password1,email=email,first_name=first_name,is_rider=is_rider,last_name=last_name,profile_pic=profile_pic)
            user.save()
            messages.success(request, "Your are now successfully registered")
            return redirect('rider_login') 
    else:
        form = RiderRegisterForm()    
    
    return render(request, 'rider/rider-signup.html', {'form':form})    
        

def rider_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request, "You are now logged in")
            return redirect('rider_dashboard')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('rider_login')
    else:            
        return render(request, 'rider/rider-login.html')
    

def rider_logout(request):
    auth.logout(request)
    messages.info(request, "You are now logged out")
    return redirect('rider_login')

@login_required(login_url='/')
def rider_dashboard(request):
    trips_progress = Trip.objects.filter(status='IN_PROGRESS') 
    trips_completed = Trip.objects.filter(status='COMPLETED')
    context = {
        'trips_progress': trips_progress,
        'trips_completed' : trips_completed
    }
    return render(request, 'rider/rider-dashboard.html', context)





