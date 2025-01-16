from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, View
from .form import ReporteForm
from .models import Reporte
from .functions import render_to_pdf
from .managers import ReporteManager

# Create your views here.
class ReporteCreateView(CreateView):
    form_class = ReporteForm
    template_name = "reporte/add-reporte.html"
    success_url = reverse_lazy("reporte_app:lista-reportes")


class ListaReporte(ListView):
    model = Reporte
    template_name = "reporte/lista-reportes.html"
    context_object_name = "reportes"

class ListaReportePDF(View):

    def get(self, request, *args, **kwargs):
        reportes = Reporte.objects.obtener_reporte()
        data = {
            "reportes": reportes
        }
        pdf = render_to_pdf("reporte/lista.html", data)
        return HttpResponse(pdf, content_type="application/pdf")
