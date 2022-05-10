from django import forms
from portal.models import Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ('nome', 'data_nascimento', 'email')
        #exclude = ()

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'autofocus': ''}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }