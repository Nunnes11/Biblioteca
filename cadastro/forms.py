from .models import Livro
from django.forms import ModelForm

class LivroForm(ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'