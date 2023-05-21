from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields=['rut', 'nombre', 'razon_social', 'clave_sii', 'email', 'telefono', 'estado']
        widgets={
            'rut': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'razon_social': forms.Textarea(attrs={'class':'form-control'}),
            'clave_sii': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }