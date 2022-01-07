from django.forms import ModelForm
from django import forms
from perpustakaan.models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

        labels = {
            'title' : 'Judul',
            'writter' : 'Penulis',
            'publisher' : 'Penerbit',
            'amount' : 'Jumlah',
            'group_id' : 'Kelompok',
        }

        widgets = {
        'title' : forms.TextInput({'class':'form-control'}),
        'writter' : forms.TextInput({'class':'form-control'}),
        'publisher' : forms.TextInput({'class':'form-control'}),
        'amount' : forms.NumberInput({'class':'form-control'}),
        'group_id' : forms.Select({'class':'form-control'}),
        }
        
    