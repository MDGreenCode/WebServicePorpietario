import re

from django import forms
from .models import Solicitud
class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_matrimonio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


def validar_cedula(cedula):
    cedula = cedula.replace('-', '').strip()

    if not re.match(r'^\d{11}$', cedula):
        raise forms.ValidationError("La cédula debe tener 11 dígitos")

    pesos = [1,2]*5 + [1]
    suma = 0

    for i in range(11):
        num = int(cedula[i]) * pesos[i]
        if num > 9:
            num = num // 10 + num % 10
        suma += num

    if suma % 10 != 0:
        raise forms.ValidationError("Cédula inválida")

class SolicitudForm(forms.ModelForm):

    class Meta:
        model = Solicitud
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        tipo = cleaned_data.get("tipo_identificacion")
        numero = cleaned_data.get("numero_identificacion")

        if tipo == "cedula":
            validar_cedula(numero)

        return cleaned_data

def clean_fecha_matrimonio(self):
    estado = self.cleaned_data.get("estado_civil")
    fecha = self.cleaned_data.get("fecha_matrimonio")

    if estado in ["casado", "union_libre"] and not fecha:
        raise forms.ValidationError("Debe indicar la fecha de matrimonio")

    return fecha

from .models import Educacion, Experiencia

class EducacionForm(forms.ModelForm):
    class Meta:
        model = Educacion
        fields = '__all__'

class ExperienciaForm(forms.ModelForm):
    class Meta:
        model = Experiencia
        fields = '__all__'