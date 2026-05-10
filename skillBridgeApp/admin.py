from django.contrib import admin
from .models import Profile, Job


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone')
    search_fields = ('user__username', 'user__email', 'phone')

    @admin.display(description='Username')
    def username(self, obj):
        return obj.user.username

    @admin.display(description='Email')
    def email(self, obj):
        return obj.user.email

    @admin.display(description='Phone')
    def phone(self, obj):
        return obj.phone


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')
    search_fields = ('title', 'description')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Job, JobAdmin)