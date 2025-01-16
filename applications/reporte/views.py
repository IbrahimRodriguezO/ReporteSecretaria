from django.shortcuts import render
from django.views.generic import CreateView
from .form import ReporteForm

# Create your views here.
class ReporteCreateView(CreateView):
    form_class = ReporteForm
    template_name = "reporte/add-reporte.html"
    success_url = "."
