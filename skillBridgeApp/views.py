from django.shortcuts import render,redirect
from .models import Job  

# Create your views here.
def home(request):
    return render(request, 'index.html')
from django.shortcuts import render

def jobs(request):
    all_jobs = Job.objects.all().order_by('-created_at') 

    return render(request, 'jobs.html', {'jobs': all_jobs})

# ... keep your home and jobs views ...

def post_gig(request):
    if request.method == 'POST':
        # 1. Grab the data the user typed into the form
        job_title = request.POST.get('title')
        job_description = request.POST.get('description')
        job_rate = request.POST.get('hourly_rate')
        job_phone = request.POST.get('phone_number')
        
        # 2. Save it to the Database!
        Job.objects.create(
            title=job_title,
            description=job_description,
            hourly_rate=job_rate,
            phone_number=job_phone
        )
        
        # 3. Redirect the user to the Job Board
        return redirect('jobs')
        
    # If they are just visiting the page normally, show them the blank form
    return render(request, 'post.html')

# ... keep your login and signup views ...

def login_view(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')