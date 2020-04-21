from django.forms import ModelForm, HiddenInput
from .models import Pets

class AddPetsForm(ModelForm):
    class Meta():
        model = Pets
        exclude = ('user',)










