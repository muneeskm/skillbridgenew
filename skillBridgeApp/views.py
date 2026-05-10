import profile

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Job, Profile
from django.contrib import messages
import re
from django.contrib.auth.decorators import login_required


# ------------------------------
# Home Page
# ------------------------------
def home(request):
    return render(request, 'index.html')

# ------------------------------
# Job Listings
# ------------------------------
def jobs(request):
    all_jobs = Job.objects.all().order_by('-created_at')
    return render(request, 'jobs.html', {'jobs': all_jobs})

# ------------------------------
# Post a Job
# ------------------------------
def post_gig(request):
    if request.method == 'POST':
        job_title = request.POST.get('title')
        job_description = request.POST.get('description')
        job_rate = request.POST.get('hourly_rate')
        job_phone = request.POST.get('phone_number')

        Job.objects.create(
            title=job_title,
            description=job_description,
            hourly_rate=job_rate,
            phone_number=job_phone
        )

        return redirect('jobs')

    return render(request, 'post.html')

# ------------------------------
# Signup (Correct)
# ------------------------------
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get("phone")

        if phone and not re.fullmatch(r"\d{10}", phone):
            return render(request, "profile.html", {
            "profile": profile,
            "user": request.user,
            "error": "Phone number must be exactly 10 digits"
        })

        profile.phone = phone

        # Validation removed for brevity...

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        # Update auto-created Profile
        user.profile.phone = phone
        user.profile.save()

        messages.success(request, "Account created successfully.")
        return redirect('login')

    return render(request, 'signup.html')
# ------------------------------
# Login (email/username/phone)
# ------------------------------
def login_view(request):
    if request.method == 'POST':
        identifier = request.POST.get('identifier')
        password = request.POST.get('password')

        # Identify whether it's phone or email
        if identifier.isdigit():  
            # phone login
            try:
                profile = Profile.objects.get(phone=identifier)
                username = profile.user.username
            except Profile.DoesNotExist:
                return render(request, 'login.html', {'error': "Invalid phone number"})
        else:
            # email login
            username = identifier

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        return render(request, 'login.html', {'error': "Incorrect password"})

    return render(request, 'login.html')

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        phone = request.POST.get("phone")
        bio = request.POST.get("bio")
        location = request.POST.get("location")

        # validation
        if phone and (not phone.isdigit() or len(phone) != 10):
            return render(request, "profile.html", {
                "profile": profile,
                "user": request.user,
                "error": "Phone must be 10 digits"
            })

        # uniqueness check
        if Profile.objects.exclude(user=request.user).filter(phone=phone).exists():
            return render(request, "profile.html", {
                "profile": profile,
                "user": request.user,
                "error": "Phone number already taken"
            })

        profile.phone = phone
        profile.bio = bio
        profile.location = location

        if request.FILES.get("profile_pic"):
            profile.profile_pic = request.FILES["profile_pic"]

        profile.save()
        return redirect('profile')

    return render(request, "profile.html", {
        "profile": profile,
        "user": request.user
    })

def public_profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = user.profile

    jobs = user.jobs_done.filter(completed=True)
    reviews = user.reviews_received.all()

    return render(request, "public_profile.html", {
        "profile_user": user,
        "profile": profile,
        "jobs": jobs,
        "reviews": reviews
    })
def custom_logout(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect("login")