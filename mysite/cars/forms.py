from django import forms
from .models import Review
from django.forms import ModelForm

# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label='First Name', max_length=100)
#     last_name = forms.CharField(label='Last Name', max_length=100)
#     emaiil = forms.EmailField(label='Email')
#     review = forms.CharField(label='Please provide your review here', widget=forms.Textarea(attrs={'class':'myform', 'rows': '2', 'cols': '20'}))

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        labels = {
            'first_name': 'Your First Name',
            'last_name': 'Your Last Name',
            'stars': 'How many stars would you give us?',
        }
        error_messages = {
            'stars': {
                'min_value': 'Min value is 1',
                'max_value': 'Max value is 5',
            }
        }