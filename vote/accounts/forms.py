from django.forms import ModelForm
from .models import pollQuetions

class CreatePollForm(ModelForm):
    class Meta:
        model=pollQuetions
        fields=['pollquetion','option1','option2','option3']
        # widget={
        #     'pollquetion':forms.CharField(attrs={
        #         'class':'form-control'
        #     })
        #     'option1':forms.CharField(attrs={
        #         'class':'form-control'
        #     })
        #     'option2':forms.CharField(attrs={
        #         'class':'form-control'
        #     })
        #     'option3':forms.CharField(attrs={
        #         'class':'form-control'
        #     })
        # }