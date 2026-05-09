from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs/', views.jobs, name='jobs'),
    path('post/', views.post_gig, name='post_gig'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
]