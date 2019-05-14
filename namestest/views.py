from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import name_formset
from .models import Name

def create_names_form(request):
    template_name = 'create_names.html'
    heading_message = 'Formset Demo'
    if request.method == 'GET':
        formset = name_formset(request.GET or None)
    elif request.method == 'POST':
        formset = name_formset(request.POST)
        if formset.is_valid():
            for form in formset:
                name = form.cleaned_data.get('name')
                if name:
                    Name(name=name).save()
            return redirect('/get')

    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })

def get_submitted_forms(request):
    serialize = serializers.serialize("json", Name.objects.all())
    data = {"data": serialize}
    return JsonResponse(data)
