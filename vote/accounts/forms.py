from django.forms import ModelForm
from .models import pollQuetions

class CreatePollForm(ModelForm):
    class Meta:
        model=pollQuetions
        fields=['pollquetion','option1','option2','option3']
    