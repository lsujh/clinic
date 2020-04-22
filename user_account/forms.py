from django.forms import ModelForm
from .models import Pets

class AddPetsForm(ModelForm):
    class Meta():
        model = Pets
        exclude = ('UserId',)










