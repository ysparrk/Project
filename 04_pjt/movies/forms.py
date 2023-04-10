from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):

    genre = forms.ChoiceField(choices=[('코미디', '코미디'), ('공포', '공포'), ('로맨스','로맨스'), ('가족', '가족'), ('액션', '액션')])
 

    score = forms.FloatField(
        widget=forms.NumberInput(
        attrs={
            'step' : 0.5,
            'min' : 0,
            'max' : 5,
            }
        )
    )

    release_date = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type' : 'date'
            }
        )
    )


    class Meta:
        model = Movie
        fields = '__all__'