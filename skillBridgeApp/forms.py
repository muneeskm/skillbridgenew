from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'bio', 'location', 'profile_pic']

    def clean_phone(self):
        phone = self.cleaned_data['phone']

        if phone and Profile.objects.exclude(pk=self.instance.pk).filter(phone=phone).exists():
            raise forms.ValidationError("This phone number is already taken.")

        return phone