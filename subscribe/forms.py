from django import forms
from .models import Subscribe



#class form

# def validating(value):
#     if ',' in value:
#         raise forms.ValidationError("invalid")
#     return value

# class SubscribeForm(forms.Form):
#     first_name = forms.CharField(max_length=50,validators=[validating])
#     last_name = forms.CharField(max_length=50,disabled=False)
#     email = forms.EmailField(max_length=50)



#model form

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ['first_name','last_name','email','option']