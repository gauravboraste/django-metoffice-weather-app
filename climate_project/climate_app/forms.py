from django import forms

class ClimateDataForm(forms.Form):
    REGION_CHOICES = [
        ('UK', 'UK'),
        ('England', 'England'),
        ('Wales', 'Wales'),
        ('Scotland', 'Scotland'),
       
    ]

    PARAMETER_CHOICES = [
        ('Tmax', 'Maximum Temperature'),
        ('Tmin', 'Minimum Temperature'),
        ('Rainfall', 'Rainfall'),
        
    ]

    region = forms.ChoiceField(choices=REGION_CHOICES, label='Region')
    parameter = forms.ChoiceField(choices=PARAMETER_CHOICES, label='Parameter')
