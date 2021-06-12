from django import forms

class TranslateForm(forms.Form):
    term = forms.CharField(label='Enter your word or expression', max_length=500)