from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import include

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/', views.jobs, name='jobs'),
    path('post/', views.post_gig, name='post_gig'),
    path('login/', views.login_view, name='login'),  # updated
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('u/<str:username>/', views.public_profile, name='public_profile'),
    path('logout/', views.custom_logout, name='logout'),
]