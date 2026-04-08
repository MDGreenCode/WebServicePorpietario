from django.shortcuts import render, redirect
from .forms import SolicitudForm

def crear_solicitud(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = SolicitudForm()

    return render(request, 'formulario/formulario.html', {'form': form})


def success(request):
    return render(request, 'formulario/success.html')

from django.forms import inlineformset_factory
from .models import Solicitud, Educacion, Experiencia

def crear_solicitud(request):

    EducacionFormSet = inlineformset_factory(Solicitud, Educacion, fields='__all__', extra=1)
    ExperienciaFormSet = inlineformset_factory(Solicitud, Experiencia, fields='__all__', extra=1)

    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        formset_edu = EducacionFormSet(request.POST)
        formset_exp = ExperienciaFormSet(request.POST)

        if form.is_valid() and formset_edu.is_valid() and formset_exp.is_valid():
            solicitud = form.save()

            formset_edu.instance = solicitud
            formset_edu.save()

            formset_exp.instance = solicitud
            formset_exp.save()

            return redirect('success')

    else:
        form = SolicitudForm()
        formset_edu = EducacionFormSet()
        formset_exp = ExperienciaFormSet()

    return render(request, 'formulario/formulario.html', {
        'form': form,
        'formset_edu': formset_edu,
        'formset_exp': formset_exp,
    })