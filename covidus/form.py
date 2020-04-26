from django.forms import ModelForm  
from covidus_main.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = []

    def __str__(self):
        return self.name
