from django.shortcuts import render, redirect, get_object_or_404
from django.forms import inlineformset_factory

from .forms import SolicitudForm
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


def success(request):
    return render(request, 'formulario/success.html')


def listado_solicitudes(request):
    """Muestra un listado con todas las solicitudes guardadas."""
    solicitudes = Solicitud.objects.all().order_by('-id')
    return render(request, 'formulario/listado.html', {
        'solicitudes': solicitudes,
    })


def detalle_solicitud(request, pk):
    """Muestra el detalle completo de una solicitud, incluyendo
    su educación y experiencia laboral asociadas."""
    solicitud = get_object_or_404(
        Solicitud.objects.prefetch_related('educaciones', 'experiencias'),
        pk=pk,
    )
    return render(request, 'formulario/detalle.html', {
        'solicitud': solicitud,
    })
