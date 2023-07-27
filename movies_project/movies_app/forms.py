from django import forms
from .models import Movies

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movies
        fields=['name','imdb','desc','year','img']