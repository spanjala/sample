from django import forms
import re
from models import Metro
#from models import Details
class NameForm(forms.Form):
    name=forms.CharField(max_length=30, min_length=4,required=True)
    city=forms.CharField(max_length=30, min_length=4,required=True)

    def clean_name(self):
        u = self.cleaned_data['name']
        print u
        if not Metro.objects.filter(name = u):
            return u
        else:
            raise forms.ValidationError("trainname is already exists")


class DetailsForm(forms.Form):
    number=forms.CharField(max_length=30, min_length=4,required=True)
    start_stage=forms.CharField(max_length=30, min_length=4,required=True)
    end_stage=forms.CharField(max_length=30, min_length=4,required=True)

    def clean_number(self):
        u = self.cleaned_data['number']
        if not Details.objects.filter(number = u):
            return
        else:
             raise forms.ValidationError("trainumber is already exists")
                              
                              
                              
        
            
